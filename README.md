# Stupid Markdown Website

Converts markdown to HTML, sticks the HTML in a template that contains all the
boilerplate, puts the generated page in the `public_html` dir.

## Dependencies

- pandoc (`sudo apt-get install pandoc`)
- that's all

## How to Use

1. Put markdown in the `markdown` folder
2. Edit config.py
3. Add a dict to the `"markdown"` list containing the following attributes
    1. `file`: The name of the file you just added to the `markdown` folder.
        **Not** the full path!
    2. `title`: The title of the page
    3. `out`: The name of the HTML file you'd like to generate.
4. Run `gen.py`
5. Party

## Other Notes

Point your webserver's config at the `public_html` directory, NOT the root
folder of this repo.

Anything in the markdown that looks like a bare URL will become a link in the
generated HTML. See line 34ish of `gen.py` for the linkification process.
