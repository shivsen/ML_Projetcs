import sys

def get_error_message(error, error_detail : sys):
    _, _, exe_tab = error_detail.exc_info()
    file_name = exe_tab.tb_frame.f_code.co_filename

    error_message = f"Error occured in {file_name}, Line Number {exe_tab.tb_lineno}, {str(error)}"
    return error_message

class CustomExceptiion (Exception):
    def __init__(self, error_message, error_detail : sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message