# -*- coding: utf-8 -*-
"""package module qacode.core.pages.page"""


from qacode.core.pages.page_config import PageConfig


class Page(object):
    """Base class for all Inehrit Page classes wich need
        selenium functionality througth qacode library
    """

    def __init__(self, browser, **kwargs):
        """Allow to use Page Object Model"""
        self._browser = browser
        self._log = self._browser.log
        self._config = PageConfig(**kwargs)

    def go_url(self, url=None, wait=0):
        """Go to url, choose url from instance or locator params

        Keyword Arguments:
            url {str} -- string of FQDN, if None, load value from settings
                (default: {self.settings.get('url')})
            wait_for_load {int} -- [description] (default: {0})
        """
        if url is None:
            url = self._config.url
        self._log.debug('page |navigate to url={}'.format(url))
        self._browser.commons.get_url(url, wait=wait)

    def is_url(self, url=None):
        """Allows to check if current selenium visible url it's
            the same what self.url value
        """
        if url is None:
            url = self._config.url
        return self._browser.commons.is_url(url)

    @property
    def config(self):
        """TODO: doc method"""
        return self._config
