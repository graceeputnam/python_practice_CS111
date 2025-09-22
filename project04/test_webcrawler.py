from byu_pytest_utils import max_score, run_python_script, test_files, this_folder, with_import, ensure_missing
from pytest import approx, fixture
from PIL import Image as PILImage, ImageChops
import matplotlib.pyplot as plt
import requests
from unittest.mock import patch
from pathlib import Path
import matplotlib.pyplot as plt

def patched_show(*_, **__):
    raise ReferenceError("Call to plt.show() in code! You should remove any calls to plt.show() and try again!")

plt.show = patched_show


def do_invalid_args_test(capsys, error_message='', *args):
    try:
        run_python_script(str(this_folder / 'webcrawler.py'), *args)
    except SystemExit:
        pass  # ignore any exceptions
    captured = capsys.readouterr()
    assert 'invalid arguments' in captured.out.lower(), f"Your program didn't print 'invalid arguments' with command line arguments {args}. {error_message}"


@max_score(10)
def test_invalid_arguments(capsys):
    do_invalid_args_test(capsys, "Invalid due to no flag.")
    do_invalid_args_test(capsys, "Invalid due to invalid flag.",
                         'asdf')
    do_invalid_args_test(capsys, "Invalid due to invalid flag.",
                         '-a')
    do_invalid_args_test(capsys, "Invalid due to not enough arguments.",
                         '-c')
    do_invalid_args_test(capsys, "Invalid due to not enough arguments.",
                         '-c', 'https://cs111.byu.edu/')
    do_invalid_args_test(capsys, "Invalid due to not enough arguments.",
                         '-p')
    do_invalid_args_test(capsys, "Invalid due to not enough arguments.",
                         '-p', 'https://cs111.byu.edu/')
    do_invalid_args_test(capsys, "Invalid due to not enough arguments.",
                         '-i')
    do_invalid_args_test(capsys, "Invalid due to not enough arguments.",
                         '-i', 'https://cs111.byu.edu/')
    do_invalid_args_test(capsys, "Invalid because '-a' is not a valid image flag.",
                         '-i', 'https://cs111.byu.edu/', 'asdf_', '-a')


@fixture(scope="session")
@with_import('RequestGuard', 'RequestGuard')
def request_guard_tests(RequestGuard):
    try:
        guard = RequestGuard('https://cs111.byu.edu')
        assert guard.forbidden == ['/Projects/project04/assets/page5.html']
        for i in range(1,5):
            assert guard.can_follow_link(f'https://cs111.byu.edu/Projects/project04/assets/page{i}.html')
        assert not guard.can_follow_link('https://cs111.byu.edu/Projects/project04/assets/page5.html')

        # Mocking a different robots.txt
        guard.forbidden = ["/data", "/images/jpg", "/Projects/Project4/Project4.md"]

        assert     guard.can_follow_link('https://cs111.byu.edu/')
        assert     guard.can_follow_link('https://cs111.byu.edu/asdf.html')
        assert     guard.can_follow_link('https://cs111.byu.edu/Projects/Project4/')
        assert     guard.can_follow_link('https://cs111.byu.edu/Projects/Project4/Project3.md')
        assert     guard.can_follow_link('https://cs111.byu.edu/images/asdf.jpg')
        assert     guard.can_follow_link('https://cs111.byu.edu/images/png/asdf.png')
        assert not guard.can_follow_link('https://byu.edu/')
        assert not guard.can_follow_link('https://cs111.byu.edu/data/')
        assert not guard.can_follow_link('https://cs111.byu.edu/data/asdf.csv')
        assert not guard.can_follow_link('https://cs111.byu.edu/images/jpg/')
        assert not guard.can_follow_link('https://cs111.byu.edu/images/jpg/asdf.jpg')
        assert not guard.can_follow_link('https://cs111.byu.edu/Projects/Project4/Project4.md')


        guard = RequestGuard("https://cs111.byu.edu/Homework/homework07/")
        assert guard.forbidden == ['/Projects/project04/assets/page5.html']

        # Mocking a different robots.txt
        guard.forbidden = ['/data', '/images/jpg', '/lectures/Stephens']
        assert     guard.can_follow_link('https://cs111.byu.edu/')
        assert     guard.can_follow_link('https://cs111.byu.edu/asdf.html')
        assert     guard.can_follow_link('https://cs111.byu.edu/Projects/Project4/')
        assert     guard.can_follow_link('https://cs111.byu.edu/lectures/Reynolds/')
        assert     guard.can_follow_link('https://cs111.byu.edu/images/asdf.jpg')
        assert     guard.can_follow_link('https://cs111.byu.edu/images/png/asdf.png')
        assert not guard.can_follow_link('https://byu.edu/')
        assert not guard.can_follow_link('https://cs111.byu.edu/data/')
        assert not guard.can_follow_link('https://cs111.byu.edu/data/asdf.csv')
        assert not guard.can_follow_link('https://cs111.byu.edu/images/jpg/')
        assert not guard.can_follow_link('https://cs111.byu.edu/images/jpg/asdf.jpg')
        assert not guard.can_follow_link('https://cs111.byu.edu/lectures/Stephens/')

    except Exception as e:
        return e


@max_score(15)
def test_request_guard(request_guard_tests):
    if type(request_guard_tests) == Exception:
        raise request_guard_tests


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


def compare_files(output_file: Path, expected_file: Path):
    try:
        with open(output_file, 'r') as out_file, open(expected_file, 'r') as expect_file:
            assert out_file.read() == expect_file.read(), "Output file does not match expected file"
        output_file.unlink(missing_ok=True)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Couldn't find the output file: {e}")


def create_safe_request(max_requests=50):
    request_count = 0
    original_get = requests.get

    def safe_request(url, stream=False):
        nonlocal request_count
        request_count += 1
        if request_count > max_requests:
            raise InterruptedError(f"Program tried making too many GET requests ({max_requests}). Aborting tests.")
        if not url.startswith("https://cs111.byu.edu"):
            raise ConnectionError(f"Tried to request non BYU url: {url}")
        return original_get(url, stream=stream)

    return safe_request


@ensure_missing(this_folder / 'count_links.output.csv')
@ensure_missing(this_folder / 'count_links.output.png')
@max_score(25)
@patch('requests.get', create_safe_request(max_requests=10))
def test_count_links(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'

    plt.clf()
    run_python_script(
        this_folder / 'webcrawler.py', '-c',
        'https://cs111.byu.edu/Projects/project04/assets/page1.html',
        this_folder / 'count_links.output.png',
        this_folder / 'count_links.output.csv'
    )

    compare_images(this_folder / 'count_links.output.png', test_files / 'count_links.key.png')
    compare_files(this_folder / 'count_links.output.csv', test_files / 'count_links.key.csv')


@ensure_missing(this_folder / 'plot_data.output.png')
@ensure_missing(this_folder / 'plot_data.output.csv')
@max_score(12.5)
@patch('requests.get', create_safe_request(max_requests=5))
def test_plot_data_two_column(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'

    plt.clf()
    run_python_script(
        this_folder / 'webcrawler.py', '-p',
        'https://cs111.byu.edu/Projects/project04/assets/data.html',
        this_folder / 'plot_data.output.png',
        this_folder / 'plot_data.output.csv'
    )

    compare_images(this_folder / 'plot_data.output.png', test_files / 'plot_data.key.png')
    compare_files(this_folder / 'plot_data.output.csv', test_files / 'plot_data.key.csv')


@ensure_missing(this_folder / 'plot_data2.output.png')
@ensure_missing(this_folder / 'plot_data2.output.csv')
@max_score(12.5)
@patch('requests.get', create_safe_request(max_requests=5))
def test_plot_data_four_column(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'

    plt.clf()
    run_python_script(
        this_folder / 'webcrawler.py', '-p',
        'https://cs111.byu.edu/Projects/project04/assets/data2.html',
        this_folder / 'plot_data2.output.png',
        this_folder / 'plot_data2.output.csv'
    )

    compare_images(this_folder / 'plot_data2.output.png', test_files / 'plot_data2.key.png')
    compare_files(this_folder / 'plot_data2.output.csv', test_files / 'plot_data2.key.csv')


def modify_images_test(images, prefix, filter):
    run_python_script(
        this_folder / 'webcrawler.py', '-i',
        'https://cs111.byu.edu/Projects/project04/assets/images.html',
        prefix, filter
    )

    for image in images:
        compare_images(this_folder / f'{prefix}{image}', test_files / f'{prefix}{image}')
        image_path = this_folder / f'{image}'
        image_path.unlink(missing_ok=True)


@ensure_missing(this_folder / 's_flamingo-float.png')
@ensure_missing(this_folder / 's_landscape.png')
@ensure_missing(this_folder / 'flamingo-float.png')
@ensure_missing(this_folder / 'landscape.png')
@max_score(6.25)
@patch('requests.get', create_safe_request(max_requests=5))
def test_modify_images_sepia(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 's_', '-s')


@ensure_missing(this_folder / 'g_flamingo-float.png')
@ensure_missing(this_folder / 'g_landscape.png')
@ensure_missing(this_folder / 'flamingo-float.png')
@ensure_missing(this_folder / 'landscape.png')
@max_score(6.25)
@patch('requests.get', create_safe_request(max_requests=5))
def test_modify_images_grayscale(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 'g_', '-g')


@ensure_missing(this_folder / 'f_flamingo-float.png')
@ensure_missing(this_folder / 'f_landscape.png')
@ensure_missing(this_folder / 'flamingo-float.png')
@ensure_missing(this_folder / 'landscape.png')
@max_score(6.25)
@patch('requests.get', create_safe_request(max_requests=5))
def test_modify_images_vertical_flip(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 'f_', '-f')


@ensure_missing(this_folder / 'm_flamingo-float.png')
@ensure_missing(this_folder / 'm_landscape.png')
@ensure_missing(this_folder / 'flamingo-float.png')
@ensure_missing(this_folder / 'landscape.png')
@max_score(6.25)
@patch('requests.get', create_safe_request(max_requests=5))
def test_modify_images_horizontal_flip(request_guard_tests):
    if type(request_guard_tests) == Exception:
        assert False, 'RequestGuard must work before the rest of the assignment can be tested'
    modify_images_test(['flamingo-float.png', 'landscape.png'], 'm_', '-m')
