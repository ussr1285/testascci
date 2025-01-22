from PIL import Image
import numpy as np

# Load the uploaded image
image_path = 'test.png'
image = Image.open(image_path)

# Resize image for better ASCII conversion
image = image.resize((80, 40))
image = image.convert('L')  # Convert to grayscale

## 정상적
ascii_chars = " .:-=+*#%@"
# ascii_chars = "░▒▓█"

## 괴상한
# ascii_chars = "가나나まみむめも▒▓█"
# ascii_chars = " -_/\|!~+=*<>:#"
# ascii_chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# ascii_chars = "▁▂▃▄▅▆▇█▓▒░ .:-=+*%@#"
# ascii_chars = "😀😁😂🤣😃😄😅😆😉😊😋😎😍"

# Convert pixels to ASCII
def pixel_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    num_chars = len(ascii_chars)  # 문자 셋의 길이 확인

    for row in pixels:
        for pixel in row:
            # 픽셀 값(0-255)을 문자 인덱스(0-문자 길이)로 변환
            char_index = int(pixel / 255 * (num_chars - 1))
            ascii_str += ascii_chars[char_index]
        ascii_str += "\n"
    return ascii_str

ascii_art = pixel_to_ascii(image)

# Save ASCII art to a text file
output_file_path = 'ascii_art.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(ascii_art)

print(f"ASCII 아트가 {output_file_path} 파일로 저장되었습니다.")
