import argparse
from social_media_sites import Twitter, Instagram, Facebook, LinkedIn, GitHub, ChessDotCom, Reddit, TikTok, Snapchat, Pinterest, Tumblr, SoundCloud, Flickr, Vimeo, MixCloud, Behance, Dribbble, DeviantArt

def search_social_media(username, options):
    results = []
    if 'twitter' in options.sites:
        results.append(Twitter.search(username))
    if 'instagram' in options.sites:
        results.append(Instagram.search(username))
    if 'facebook' in options.sites:
        results.append(Facebook.search(username))
    if 'linkedin' in options.sites:
        results.append(LinkedIn.search(username))
    if 'github' in options.sites:
        results.append(GitHub.search(username))
    if 'chessdotcom' in options.sites:
        results.append(ChessDotCom.search(username))
    if 'reddit' in options.sites:
        results.append(Reddit.search(username))
    if 'tiktok' in options.sites:
        results.append(TikTok.search(username))
    if 'snapchat' in options.sites:
        results.append(Snapchat.search(username))
    if 'pinterest' in options.sites:
        results.append(Pinterest.search(username))
    if 'tumblr' in options.sites:
        results.append(Tumblr.search(username))
    if 'soundcloud' in options.sites:
        results.append(SoundCloud.search(username))
    if 'flickr' in options.sites:
        results.append(Flickr.search(username))
    if 'vimeo' in options.sites:
        results.append(Vimeo.search(username))
    if 'mixcloud' in options.sites:
        results.append(MixCloud.search(username))
    if 'behance' in options.sites:
        results.append(Behance.search(username))
    if 'dribbble' in options.sites:
        results.append(Dribbble.search(username))
    if 'deviantart' in options.sites:
        results.append(DeviantArt.search(username))

    # Print the results
    for result in results:
        print(result)

def main():
    parser = argparse.ArgumentParser(description='Find Usernames Across Social Networks')
    parser.add_argument('usernames', nargs='+', help='One or more usernames to check with social networks.')
    parser.add_argument('--sites', nargs='+', default=['twitter', 'instagram', 'facebook', 'linkedin', 'github', 'chessdotcom', 'reddit', 'tiktok', 'snapchat', 'pinterest', 'tumblr', 'soundcloud', 'flickr', 'vimeo', 'mixcloud', 'behance', 'dribbble', 'deviantart'],
                        choices=['twitter', 'instagram', 'facebook', 'linkedin', 'github', 'chessdotcom', 'reddit', 'tiktok', 'snapchat', 'pinterest', 'tumblr', 'soundcloud', 'flickr', 'vimeo', 'mixcloud', 'behance', 'dribbble', 'deviantart'],
                        help='Limit analysis to specific social media sites.')
    args = parser.parse_args()

    for username in args.usernames:
        search_social_media(username, args)

if __name__ == '__main__':
    main()
