from byu_pytest_utils import max_score, this_folder, test_files, with_import, ensure_missing
from PIL import Image as PILImage, ImageChops
from pytest import approx
from pathlib import Path
import matplotlib.pyplot as plt

def patched_show(*_, **__):
    raise ReferenceError("Call to plt.show() in code! You should remove any calls to plt.show() and try again!")

plt.show = patched_show


def compare_images(obs: Path | PILImage.Image, exp: Path | PILImage.Image):
    if not isinstance(obs, PILImage.Image):
        observed = PILImage.open(obs).convert('RGB')
    else:
        observed = obs
    if not isinstance(exp, PILImage.Image):
        expected = PILImage.open(exp).convert('RGB')
    else:
        expected = exp

    assert observed.size == expected.size, f"Image sizes don't match. Expected `{expected.size}`, but got `{observed.size}`."

    diff = ImageChops.difference(observed, expected)
    if bbox := diff.getbbox():
        for y in range(bbox[1], bbox[3]):
            for x in range(bbox[0], bbox[2]):
                observed_pixel = observed.getpixel((x, y))
                expected_pixel = expected.getpixel((x, y))
                if not observed_pixel or not expected_pixel:
                    assert False, f"Failed to get pixels at ({x}, {y})!"

                if isinstance(observed_pixel, (float, int)) or isinstance(expected_pixel, (float, int)):
                    assert False, "Failed to get correct pixel type!"

                assert observed_pixel[0] == approx(expected_pixel[0], abs=2), f"The pixels' red values at ({x}, {y}) don't match. Expected `{expected_pixel[0]}`, but got `{observed_pixel[0]}`."
                assert observed_pixel[1] == approx(expected_pixel[1], abs=2), f"The pixels' green values at ({x}, {y}) don't match. Expected `{expected_pixel[1]}`, but got `{observed_pixel[1]}`."
                assert observed_pixel[2] == approx(expected_pixel[2], abs=2), f"The pixels' blue values at ({x}, {y}) don't match. Expected `{expected_pixel[2]}`, but got `{observed_pixel[2]}`."

    if isinstance(obs, Path):
        obs.unlink(missing_ok=True)


@max_score(6)
@with_import('lab23', 'plot_histogram')
@ensure_missing(this_folder / 'sat_score.png')
@ensure_missing(this_folder / 'gpa.png')
def test_plot_histogram(plot_histogram):
    sat_key = test_files / 'sat_score.key.png'
    gpa_key = test_files / 'gpa.key.png'

    plot_histogram()

    sat_observed = this_folder / 'sat_score.png'
    gpa_observed = this_folder / 'gpa.png'

    compare_images(sat_observed, sat_key)
    compare_images(gpa_observed, gpa_key)


@max_score(6)
@with_import('lab23', 'plot_scatter')
@ensure_missing(this_folder / 'correlation.png')
def test_plot_scatter(plot_scatter):
    correlation_key = test_files / 'correlation.key.png'
    plot_scatter()
    correlation_observed = this_folder / 'correlation.png'
    compare_images(correlation_observed, correlation_key)


@max_score(8)
@with_import('lab23', 'plot_spectra')
@ensure_missing(this_folder / 'spectra.png')
def test_plot_spectra(plot_spectra):
    spectra_key = test_files / 'spectra.key.png'
    plot_spectra()
    spectra_observed = this_folder / 'spectra.png'
    compare_images(spectra_observed, spectra_key)
