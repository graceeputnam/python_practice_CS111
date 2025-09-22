from PIL import Image as PILImage, ImageChops
from byu_pytest_utils import max_score, test_files, with_import
from pytest import approx


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


@max_score(10)
@with_import('homework2', 'flipped')
def test_flipped_with_landscape(flipped):
    observed = flipped(test_files / 'landscape.png')
    assert_equal(observed.image, test_files / 'landscape_flipped.key.png')


@max_score(10)
@with_import('homework2', 'flipped')
def test_flipped_with_flamingo_float(flipped):
    observed = flipped(test_files / 'flamingo-float.png')
    assert_equal(observed.image, test_files / 'flamingo-float_flipped.key.png')


@max_score(10)
@with_import('homework2', 'make_borders')
def test_make_borders_landscape(make_borders):
    observed = make_borders(test_files / 'landscape.png', 30, 0, 255, 0)
    assert_equal(observed.image, test_files / 'landscape_border.key.png')


@max_score(10)
@with_import('homework2', 'make_borders')
def test_make_borders_flamingo_float_10(make_borders):
    observed = make_borders(test_files / 'flamingo-float.png', 10, 0, 255, 255)
    assert_equal(observed.image, test_files / 'flamingo-float_border_10.key.png')


@max_score(10)
@with_import('homework2', 'make_borders')
def test_make_borders_flamingo_float_5(make_borders):
    observed = make_borders(
        test_files / 'flamingo-float.png', 5, 255, 125, 125)
    assert_equal(observed.image, test_files / 'flamingo-float_border_5.key.png')
