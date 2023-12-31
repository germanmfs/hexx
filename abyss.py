import requests

class BaseSite:
    @staticmethod
    def search(username):
        raise NotImplementedError("Subclasses must implement the search method.")

class Twitter(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://twitter.com/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Twitter: {url}'
        return f'[-] Twitter: {username} not found on Twitter.'

class Instagram(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.instagram.com/{username}/'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Instagram: {url}'
        return f'[-] Instagram: {username} not found on Instagram.'

class Facebook(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.facebook.com/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Facebook: {url}'
        return f'[-] Facebook: {username} not found on Facebook.'

class LinkedIn(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.linkedin.com/in/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] LinkedIn: {url}'
        return f'[-] LinkedIn: {username} not found on LinkedIn.'

class GitHub(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://github.com/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] GitHub: {url}'
        return f'[-] GitHub: {username} not found on GitHub.'

class ChessDotCom(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.chess.com/member/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Chess.com: {url}'
        return f'[-] Chess.com: {username} not found on Chess.com.'

class Reddit(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.reddit.com/user/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Reddit: {url}'
        return f'[-] Reddit: {username} not found on Reddit.'

class TikTok(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.tiktok.com/@{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] TikTok: {url}'
        return f'[-] TikTok: {username} not found on TikTok.'

class Snapchat(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.snapchat.com/add/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Snapchat: {url}'
        return f'[-] Snapchat: {username} not found on Snapchat.'

class Pinterest(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.pinterest.com/{username}/'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Pinterest: {url}'
        return f'[-] Pinterest: {username} not found on Pinterest.'

class Tumblr(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://{username}.tumblr.com/'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Tumblr: {url}'
        return f'[-] Tumblr: {username} not found on Tumblr.'

class SoundCloud(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://soundcloud.com/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] SoundCloud: {url}'
        return f'[-] SoundCloud: {username} not found on SoundCloud.'

class Flickr(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.flickr.com/photos/{username}/'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Flickr: {url}'
        return f'[-] Flickr: {username} not found on Flickr.'

class Vimeo(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://vimeo.com/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Vimeo: {url}'
        return f'[-] Vimeo: {username} not found on Vimeo.'

class MixCloud(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.mixcloud.com/{username}/'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] MixCloud: {url}'
        return f'[-] MixCloud: {username} not found on MixCloud.'

class Behance(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://www.behance.net/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Behance: {url}'
        return f'[-] Behance: {username} not found on Behance.'

class Dribbble(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://dribbble.com/{username}'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] Dribbble: {url}'
        return f'[-] Dribbble: {username} not found on Dribbble.'

class DeviantArt(BaseSite):
    @staticmethod
    def search(username):
        url = f'https://{username}.deviantart.com/'
        response = requests.get(url)
        if response.status_code == 200:
            return f'[+] DeviantArt: {url}'
        return f'[-] DeviantArt: {username} not found on DeviantArt.'
