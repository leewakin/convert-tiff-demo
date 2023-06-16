import sys
import io
from PIL import Image


class ImageConversionError(Exception):
    pass


def convert_and_zip(image_bytes):
    """
    Convert image to 24-bit depth, 300dpi TIFF format.

    Args:
        image_bytes (bytes): The image data to be converted.

    Returns:
        bytes: The converted image data.
    """
    try:
        with Image.open(io.BytesIO(image_bytes)) as img:
            img = img.resize(
                (img.width * 3, img.height * 3), resample=Image.BICUBIC)
            img = img.convert('RGB')
            tiff_buffer = io.BytesIO()
            img.save(tiff_buffer, format='TIFF', dpi=(300, 300))
    except Exception as e:
        raise ImageConversionError("Error converting image: {}".format(e))

    # Return img as byte stream
    return tiff_buffer.getbuffer()


if __name__ == '__main__':
    # Get image data from standard input
    input_bytes = sys.stdin.buffer.read()

    # Call conversion function
    try:
        converted_buffer = convert_and_zip(input_bytes)
        sys.stdout.buffer.write(converted_buffer)
    except ImageConversionError as e:
        sys.stderr.write("Error: {}\n".format(e))
