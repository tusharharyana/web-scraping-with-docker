# Web Scraping with Docker and MongoDB Atlas

This project automates the process of scraping data from a website and storing it in MongoDB Atlas. It is containerized using Docker to ensure that the environment is consistent and portable.

## Features
- Web scraping using Python with BeautifulSoup.
- MongoDB Atlas for cloud database storage.
- Dockerized environment for ease of use and portability.
- Optional: Scheduled scraping via GitHub Actions.

## Requirements
- Docker
- Docker Compose (optional for local setup)
- GitHub account (for GitHub Actions)
- MongoDB Atlas account

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/tusharharyana/web-scraping-with-docker.git
    cd web-scraping-with-docker
    ```

2. Build and run the Docker container:
    ```bash
    docker-compose up --build -d
    ```

3. The scraper will run periodically and store the scraped data in MongoDB Atlas.

## How to Use

1. Replace the `url` variable in `scraper.py` with the URL of the website you want to scrape.
2. Replace the `<username>` and `<password>` placeholders in the MongoDB URI with your MongoDB Atlas credentials.
3. Run the scraper locally using Docker or rely on GitHub Actions for automated scraping.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or enhancements.


## Contact

For any questions or feedback, please reach out to [haryanatushar@gmail.com](mailto:haryanatushar@gmail.com).   