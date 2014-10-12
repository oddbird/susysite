# -*- coding: utf-8 -*-
"""
Multi-author module for rstblog.

Based on `rstblog.modules.tags` by Armin Ronacher.

"""
from urlparse import urljoin

from jinja2 import contextfunction

from werkzeug.contrib.atom import AtomFeed

from rstblog.signals import (
    after_file_published, before_build_finished)
from rstblog.utils import Pagination


class Author(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count


@contextfunction
def get_authors(context, limit=50):
    authors = get_author_summary(context['builder'])
    if limit:
        authors.sort(key=lambda x: -x.count)
        authors = authors[:limit]
    authors.sort(key=lambda x: x.name.lower())
    return authors


def get_author_summary(builder):
    storage = builder.get_storage('authors')
    by_author = storage.get('by_author', {})
    result = []
    for author, authored in by_author.iteritems():
        result.append(Author(author, len(authored)))
    result.sort(key=lambda x: x.count)
    return result


def get_authored_entries(builder, author):
    if isinstance(author, Author):
        author = author.name
    storage = builder.get_storage('authors')
    by_author = storage.get('by_author', {})
    return by_author.get(author) or []


def remember_authors(context):
    author = context.config.get('author') or None
    if author and context.pub_date:
        storage = context.builder.get_storage('authors')
        by_file = storage.setdefault('by_file', {})
        by_file[context.source_filename] = author
        by_author = storage.setdefault('by_author', {})
        by_author.setdefault(author, []).append(context)
        context.author = author


def write_authors_page(builder):
    with builder.open_link_file('authors') as f:
        rv = builder.render_template('authors.html')
        f.write(rv.encode('utf-8') + '\n')


def write_author_feed(builder, author):
    blog_author = builder.config.root_get('author')
    url = builder.config.root_get('canonical_url') or 'http://localhost/'
    name = builder.config.get('feed.name') or u'Recent Blog Posts'
    subtitle = builder.config.get('feed.subtitle') or u'Recent blog posts'
    feed = AtomFeed(name,
                    subtitle=subtitle,
                    feed_url=urljoin(url, builder.link_to('blog_feed')),
                    url=url)
    for entry in get_authored_entries(builder, author)[:10]:
        feed.add(entry.title, unicode(entry.render_contents()),
                 content_type='html', author=blog_author,
                 url=urljoin(url, entry.slug),
                 updated=entry.pub_date)
    with builder.open_link_file('authorfeed', author=author.name) as f:
        f.write(feed.to_string().encode('utf-8') + '\n')


def write_author_page(builder, author):
    use_pagination = builder.config.root_get('modules.blog.use_pagination', True)
    per_page = builder.config.root_get('modules.blog.per_page', 10)
    entries = get_authored_entries(builder, author)
    entries.sort(key=lambda x: x.pub_date, reverse=True)
    pagination = Pagination(
        builder, entries, 1, per_page, 'author', {'author': author.name})
    while True:
        with builder.open_link_file(
                'author', author=author.name, page=pagination.page) as f:
            rv = builder.render_template('author.html', {
                'author':           author,
                'pagination':       pagination,
                'show_pagination':  use_pagination,
            })
            f.write(rv.encode('utf-8') + '\n')
            if not use_pagination or not pagination.has_next:
                break
            pagination = pagination.get_next()


def write_author_files(builder):
    write_authors_page(builder)
    for author in get_author_summary(builder):
        write_author_page(builder, author)
        write_author_feed(builder, author)


def setup(builder):
    after_file_published.connect(remember_authors)
    before_build_finished.connect(write_author_files)
    builder.register_url(
        'author',
        config_key='modules.author.author_url',
        config_default='/authors/<author>/',
        defaults={'page': 1},
        )
    builder.register_url(
        'author',
        config_key='modules.author.paged_author_url',
        config_default='/authors/<author>/page/<page>/',
        )
    builder.register_url(
        'authorfeed',
        config_key='modules.author.author_feed_url',
        config_default='/authors/<author>/feed.atom',
        )
    builder.register_url(
        'authors',
        config_key='modules.author.authors_url',
        config_default='/authors/',
        )
    builder.jinja_env.globals['get_authors'] = get_authors
