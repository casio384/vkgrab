#!/usr/bin/python
import re
import vk
import subprocess
import sys
import os
from optparse import OptionParser
import getpass
from termcolor import colored

your_app_id="YOUR-APP-ID!!!"

def main():
    parser = OptionParser(usage='Usage: %prog -l login [OPTIONS]')
    parser.add_option('-l', '--login', dest='login', action='store', type='string', help='your login')
    parser.add_option('-s', '--search_title', dest='search_title', action='store', type='string', default=None, help='Search audio with this title')
    parser.add_option('-o', '--owner_id', dest='ownerid', action='store', type='int', default=None, help='grab data from this id;')
    parser.add_option('', '--album_name', dest='album_name', action='store', type='string', help='Name of album for download;')
    (options, args) = parser.parse_args()

    if options.login == None:
        parser.print_help()
        sys.exit()
    
    print 'Connect with login ' + options.login + '. '
    password = getpass.getpass(prompt='Password required:')

    auth_session = vk.AuthSession(app_id=your_app_id, user_login=options.login, user_password=password, scope='audio')
    access_token, _ = auth_session.get_access_token()
    session = vk.Session(access_token=access_token)
    vk_api = vk.API(session, lang='ru')
    audio_grab = AudioGrab(vk_api, options.ownerid, options.album_name, options.search_title) 
    audio_grab.run()

class AudioGrab:
    def __init__(self, api, ownerid=None, album_name=None, search_title=None):
        self.api = api
        self.ownerid = ownerid
        self.album_name = album_name
        self.album_id = None
        self.search_title = search_title
        if album_name != None:
            albums_list = self.api.audio.getAlbums(owner_id=ownerid)
            for a in albums_list[1:]:
                if a['title'] == album_name:
                    self.album_id = a['album_id']
                    break

    def run(self):
        usr_name = self.api.users.get(user_ids=self.ownerid)
        usr_name = usr_name[0]['first_name'] + '_' + usr_name[0]['last_name']
        path = './' + usr_name
        if not os.path.exists(path):
            os.makedirs(path)
        records = self.api.audio.get(count=5000, album_id=self.album_id, owner_id=self.ownerid)
        for record in records[1:]:
            track_name = record['artist'] + ' - ' + record['title']
            url = record['url']
            if self.search_title != None and re.search(self.search_title, track_name) == None:
                continue
            print colored('Download: ' + track_name, 'yellow')
            subprocess.call(['wget', '-O', path + '/' + track_name + '.mp3', url])
        
if __name__ == "__main__":
    main()
