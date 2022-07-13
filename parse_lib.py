import os
import click
import requests
from typing import Dict, Optional


API_KEY = os.environ.get("LFM_API_KEY")
USER_AGENT = 'Unpopular_interest'


class LastFmClient:
    HEADERS = {'user-agent': USER_AGENT}
    BASE_URL = 'https://ws.audioscrobbler.com/2.0/'

    def __init__(self, tag: str,
                 limit: Optional[int] = 10,
                 page: Optional[int] = 1):
        self.tag = tag
        self.limit = limit
        self.page = page

    def get_unpopular_artists_by_tag(self) -> Dict:
        """Getting artists by providing genre/tag"""

        payload = {
            'method': 'tag.gettopartists',
            'api_key': API_KEY,
            'format': 'json',
            'tag': self.tag,
            'limit': self.limit,
            'page': self.page
        }
        try:
            response = requests.get(url=self.BASE_URL,
                                    headers=self.HEADERS,
                                    params=payload)
            return response.json()
        except Exception as exc:
            raise Exception('Houston, we have some problems with getting data', exc)

    def get_general_info(self):
        print(self.get_unpopular_artists_by_tag()["topartists"]["@attr"])

    def get_list_of_artists_full_info(self):
        """Getting full artists info"""
        return self.get_unpopular_artists_by_tag()["topartists"]["artist"]

    def get_list_of_artists_names(self, top_num: Optional[int] = None):
        """Getting artists names only"""
        list_of_artists = self.get_list_of_artists_full_info()
        artist_names = [artist["name"] for artist in list_of_artists]
        for artist_name in artist_names:
            print(artist_name)

    def get_list_of_artists(self, top_num: Optional[int] = None):
        """Getting top number of artists with links to last fm profiles"""
        list_of_artists = self.get_list_of_artists_full_info()
        list_of_urls = [
            f'{artist["name"]} -> {artist["url"]}' for artist in list_of_artists
        ]
        for url in list_of_urls:
            print(url)


@click.command()
@click.option('-t', '--tag', required=True, help='tag is a requirement option')
@click.option('-l', '--limit', default=10, show_default=True,
              help='The number of results to fetch per page.')
@click.option('-p', '--page', default=1, show_default=True,
              help='Number of pages to show')
@click.option('-a', '--artists', is_flag=True, default=False, show_default=True,
              help='Show artists names')
@click.option('-i', '--info', is_flag=True, default=False, show_default=True,
              help='Show general info')
def parse_data(artists: bool,
               info: bool,
               tag: str,
               limit: int = 10,
               page: int = 1,
               ):
    client = LastFmClient(tag=tag, limit=limit, page=page)
    count_artists = limit * page

    if info:
        client.get_general_info()

    if artists:
        click.secho(f"\nTop {count_artists} artists by {tag=}:",
                    fg='green')
        client.get_list_of_artists()


if __name__ == "__main__":
    parse_data()
