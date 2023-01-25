import os
import json
import schedule
import time
from social_media_accounts import SocialMediaAccounts

class SocialMediaManager:
    def __init__(self):
        self.accounts = SocialMediaAccounts()
        self.business_info = {}
        self.load_business_info()
        self.create_social_media_accounts()
        self.schedule_posts()

    def load_business_info(self):
        with open('business_info.json') as json_file:
            self.business_info = json.load(json_file)

    def create_social_media_accounts(self):
        self.accounts.create_twitter_account(self.business_info["twitter"])
        self.accounts.create_facebook_account(self.business_info["facebook"])
        self.accounts.create_instagram_account(self.business_info["instagram"])
        self.accounts.create_linkedin_account(self.business_info["linkedin"])

    def schedule_posts(self):
        with open('post_schedule.json') as json_file:
            post_schedule = json.load(json_file)
        for post in post_schedule:
            schedule.every().day.at(post["time"]).do(self.post_to_social_media, post["platform"], post["content"])
        while True:
            schedule.run_pending()
            time.sleep(1)

    def post_to_social_media(self, platform, content):
        if platform == "twitter":
            self.accounts.post_to_twitter(content)
        elif platform == "facebook":
            self.accounts.post_to_facebook(content)
        elif platform == "instagram":
            self.accounts.post_to_instagram(content)
        elif platform == "linkedin":
            self.accounts.post_to_linkedin(content)
        else:
            print("Invalid platform")

    def track_analytics(self):
        twitter_analytics = self.accounts.get_twitter_analytics()
        facebook_analytics = self.accounts.get_facebook_analytics()
        instagram_analytics = self.accounts.get_instagram_analytics()
        linkedin_analytics = self.accounts.get_linkedin_analytics()

        print("Twitter Analytics: ", twitter_analytics)
        print("Facebook Analytics: ", facebook_analytics)
        print("Instagram Analytics: ", instagram_analytics)
        print("LinkedIn Analytics: ", linkedin_analytics)

    def manage_followers(self):
        twitter_followers = self.accounts.get_twitter_followers()
        facebook_followers = self.accounts.get_facebook_followers()
        instagram_followers = self.accounts.get_instagram_followers()
        linkedin_followers = self.accounts.get_linkedin_followers()

        print("Twitter Followers: ", twitter_followers)
        print("Facebook Followers: ", facebook_followers)
        print("Instagram Followers: ", instagram_followers)
        print("LinkedIn Followers: ", linkedin_followers)
    def run(self):
    while True:
        self.track_analytics()
        self.manage_followers()
        time.sleep(60)

if __name__ == "__main__":
    manager = SocialMediaManager()
    manager.run()
