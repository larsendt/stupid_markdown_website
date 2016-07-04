#!/usr/bin/env python
from __future__ import print_function

import subprocess
import os
import config
import re

def make_folders():
    for folder in ["public_html", "cache"]:
        if not os.path.exists(folder):
            print("Creating folder:", folder)
            os.makedirs(folder)


def markdown_to_html(in_fname, out_fname):
    print("Converting '%s' to HTML as '%s'" % (in_fname, out_fname))
    cmd = ["pandoc", in_fname, "-o", out_fname]
    subprocess.call(cmd)


def template_process(title, in_fname, out_fname):
    print("Templating '%s'. Will become '%s'" % (in_fname, out_fname))

    with open("template.html", "r") as f:
        template = f.read()

    with open(in_fname, "r") as f:
        document = f.read()

    template = template.replace("{title}", title)
    template = template.replace("{body}", document)

    # Look for links that aren't in hrefs of anchor tags (this is kinda dumb,
    # but it works okay).
    unlinked_links = re.findall("[^\"'](http[s]?://[^ \"'<]+)", document)
    for link in unlinked_links:
        linktext = "<a href=\"%s\">%s</a>" % (link, link)
        template = template.replace(link, linktext)

    with open(out_fname, "w") as f:
        f.write(template)

    
def make_htmls():
    for obj in config.get()["markdown"]:
        fname = obj["file"]
        title = obj["title"]
        outfname = obj["out"]

        fpath = "./markdown/" + fname
        outfpath = "./cache/" + outfname
        pub_fpath = "./public_html/" + outfname

        markdown_to_html(fpath, outfpath)
        template_process(title, outfpath, pub_fpath)

def main():
    make_folders()
    make_htmls()

if __name__ == "__main__":
    main()
