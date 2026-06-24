import os
from unittest.mock import patch, mock_open
from src.analytics import inject_google_tag, GTAG_ID, GTAG_CODE


def test_inject_google_tag_patches_file():
    """Test that inject_google_tag successfully patches the file if it exists and GTAG is not present."""
    mock_html = "<html><head><title>Test</title></head><body></body></html>"
    
    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=mock_html)) as mock_file:
         
        inject_google_tag()
        
        # Verify that read and write calls were made
        assert len(mock_file.call_args_list) > 0
        first_call_args = mock_file.call_args_list[0][0]
        opened_path = os.path.normpath(first_call_args[0])
        assert opened_path.endswith(os.path.join("static", "index.html"))
        
        # Verify write content contains Google Tag
        handle = mock_file()
        written = "".join([call.args[0] for call in handle.write.call_args_list])
        assert GTAG_ID in written
        assert "<head>" in written


def test_inject_google_tag_skips_if_already_patched():
    """Test that inject_google_tag does not re-patch the file if GTAG is already present."""
    mock_html_with_tag = f"<html><head>{GTAG_CODE}</head><body></body></html>"
    
    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", mock_open(read_data=mock_html_with_tag)) as mock_file:
         
        inject_google_tag()
        
        # The file should be read, but write should not be called to avoid duplication
        handle = mock_file()
        handle.write.assert_not_called()


def test_inject_google_tag_handles_exception_gracefully():
    """Test that inject_google_tag swallows exceptions (like PermissionError) without crashing."""
    with patch("os.path.exists", return_value=True), \
         patch("builtins.open", side_effect=PermissionError("Permission denied")), \
         patch("streamlit.components.v1.html") as mock_st_html:
         
        # This call should run and handle the exception internally
        inject_google_tag()
        
        # Since static patching failed, it should call fallback components.html
        mock_st_html.assert_called_once()
