import warnings
# Disable a FutureWarning
with warnings.catch_warnings():
    warnings.filterwarnings(action="ignore", category=FutureWarning)
    from scss import Compiler



def convert_scss_to_css(file_name):
    """Use pyScss to convert scss files to css files

    Parameters
    ----------
    file_name: path or list of path

    Returns
    -------
    convert file(s) in path or in all paths from "scss" to

    """
    if isinstance(file_name, list):
        for file in file_name:
            convert_scss_to_css(file)
    else:

        # Check that the file type is scss and raise an error if it is not the case
        if file_name.endswith("scss") is False:
            raise TypeError(
                f"The file {file_name} is not of type scss, please verify its extension"
            )

        with open(file_name) as scss_file:
            scss_str = scss_file.read().replace("\n", " ")

        css_str = Compiler(output_style="compressed").compile_string(scss_str)
        file_name = file_name.replace(".scss", ".css")

        with open(file_name, "w") as css_file:
            css_file.write(css_str)
