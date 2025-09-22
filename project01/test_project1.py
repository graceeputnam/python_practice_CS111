from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import max_score, run_python_script, test_files, ensure_missing, this_folder, with_import
import functools
from pytest import approx, fail
from pathlib import Path

def assert_equal(observed, expected):
    if not isinstance(observed, PILImage.Image):
        observed = PILImage.open(observed).convert('RGB')
    if not isinstance(expected, PILImage.Image):
        expected = PILImage.open(expected).convert('RGB')

    assert observed.size == expected.size, f"Image sizes don't match. Expected `{expected.size}`, but got `{observed.size}`."

    diff = ImageChops.difference(observed, expected)
    bbox = diff.getbbox()
    if bbox:
        for y in range(bbox[1], bbox[3]):
            for x in range(bbox[0], bbox[2]):
                observed_pixel = observed.getpixel((x, y))
                expected_pixel = expected.getpixel((x, y))
                assert observed_pixel[0] == approx(expected_pixel[0], abs=2), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel[0]}`, but got `{observed_pixel[0]}`."
                assert observed_pixel[1] == approx(expected_pixel[1], abs=2), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel[1]}`, but got `{observed_pixel[1]}`."
                assert observed_pixel[2] == approx(expected_pixel[2], abs=2), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel[2]}`, but got `{observed_pixel[2]}`."

@max_score(20)
@with_import('byuimage', 'Image')
def test_display_image(Image, monkeypatch):
    observed = None

    @functools.wraps(Image.show)
    def patched_Image_show(self):
        nonlocal observed
        observed = self.image
    monkeypatch.setattr(Image, 'show', patched_Image_show)

    run_python_script('image_processing.py', '-d',
                      test_files / 'explosion.input.jpg')

    if observed is None:
        fail('No Image was shown')

    assert_equal(observed, test_files / 'explosion.input.jpg')


def make_filter_tester(observed_file, key_file, *script_args):
    def decorator(func):
        @functools.wraps(func)
        def inner_func():
            run_python_script('image_processing.py', *script_args)
            assert_equal(observed_file, key_file)
            Path(observed_file).unlink(missing_ok=True)
        return inner_func
    return decorator


@max_score(5)
@ensure_missing(this_folder / "darkened-explosion.output.png")
@make_filter_tester(
    'darkened-explosion.output.png', test_files / 'darkened-explosion.key.png',
    '-k', test_files / 'explosion.input.jpg', this_folder / 'darkened-explosion.output.png', 0.3
)
def test_darken_filter():
    ...


@max_score(5)
@ensure_missing(this_folder / "sepia-explosion.output.png")
@make_filter_tester(
    'sepia-explosion.output.png', test_files / 'sepia-explosion.key.png',
    '-s', test_files / 'explosion.input.jpg', this_folder / 'sepia-explosion.output.png'
)
def test_sepia_filter():
    ...


@max_score(5)
@ensure_missing(this_folder / "grayscale-explosion.output.png")
@make_filter_tester(
    'grayscale-explosion.output.png', test_files / 'grayscale-explosion.key.png',
    '-g', test_files / 'explosion.input.jpg', this_folder / 'grayscale-explosion.output.png'
)
def test_grayscale_filter():
    ...


@max_score(5)
@ensure_missing(this_folder / "bordered-explosion.output.png")
@make_filter_tester(
    'bordered-explosion.output.png', test_files / 'bordered-explosion.key.png',
    '-b', test_files / 'explosion.input.jpg', this_folder / 'bordered-explosion.output.png', 10, 120, 20, 14
)
def test_border_filter():
    ...


@max_score(5)
@ensure_missing(this_folder / "flipped-explosion.output.png")
@make_filter_tester(
    'flipped-explosion.output.png', test_files / 'flipped-explosion.key.png',
    '-f', test_files / 'explosion.input.jpg', this_folder / 'flipped-explosion.output.png'
)
def test_flip_filter():
    ...


@max_score(15)
@ensure_missing(this_folder / "mirrored-explosion.output.png")
@make_filter_tester(
    'mirrored-explosion.output.png', test_files / 'mirrored-explosion.key.png',
    '-m', test_files / 'explosion.input.jpg', this_folder / 'mirrored-explosion.output.png'
)
def test_mirror_filter():
    ...


@max_score(20)
@ensure_missing(this_folder / "collage.output.png")
@make_filter_tester(
    'collage.output.png', test_files / 'collage.key.png',
    '-c', test_files / 'beach1.input.jpg', test_files / 'beach2.input.jpg',
    test_files / 'beach3.input.jpg', test_files / 'beach4.input.jpg',
    this_folder / 'collage.output.png', 10
)
def test_collage_filter():
    ...


@max_score(20)
@ensure_missing(this_folder / "greenscreen.output.png")
@make_filter_tester(
    'greenscreen.output.png', test_files / 'greenscreen.key.png',
    '-y', test_files / 'man.input.jpg', test_files / 'explosion.input.jpg',
    this_folder / 'greenscreen.output.png', 90, 1.3
)
def test_greenscreen_filter():
    ...
