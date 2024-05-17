# DCInside Scraper

This package scrapes posts from DCInside and saves them as a TSV file.

## Installation
pip install dcinside_scraper

or

pip install git+https://github.com/yourusername/dcinside_scraper.git

## Usage

dcinside-scraper 'https://gall.dcinside.com/mgallery/board/lists/?id=thesingularity' 1 5 output.tsv --sleep 1

- `gallery_url`: The URL of the DCInside gallery
- `start_page`: The starting page number
- `end_page`: The ending page number
- `output_file`: The output TSV file
- `--sleep`: (Optional) Time to sleep between page requests (in seconds)

## Example

To scrape posts from the DCInside gallery with the ID "thesingularity" from page 1 to page 5 and save the results to `output.tsv` with a 1-second delay between requests, use the following command:

dcinside-scraper 'https://gall.dcinside.com/mgallery/board/lists/?id=thesingularity' 1 5 output.tsv --sleep 1

## Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`
- `pandas`

These dependencies will be installed automatically when you install the package via `pip`.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

For any questions or suggestions, please open an issue or contact the repository owner.
