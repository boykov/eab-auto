#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

# Let's start with a simple example. Here's a short program to print a list of all of the documents in your Google Documents account:
# При работе через eev, возможны зависания, поскольку expect будет ожидать результата, а возможны "тормоза".
import gdata.docs.service

import gdata.contacts
import gdata.contacts.service

# Create a client class which will make HTTP requests with Google Docs server.
client = gdata.docs.service.DocsService()
# Authenticate using your Google Docs email address and password.
client.ClientLogin('eugeniy.boykov@gmail.com','pass')

# Query the server for an Atom feed containing a list of your documents.
documents_feed = client.GetDocumentListFeed()
# Loop through the feed and extract each document entry.
for document_entry in documents_feed.entry:
    # Display the title of the document on the command line.
    print document_entry.title.text

gd_client = gdata.contacts.service.ContactsService()

gd_client.ClientLogin('eugeniy.boykov@gmail.com','pass')

print gd_client.GetFeedUri()

query = gdata.contacts.service.ContactsQuery()
query.max_results = 400
cf = gd_client.GetContactsFeed(query.ToUri())

for i,entry in enumerate(cf.entry): print entry.title.text

print gd_client.GetContact('/m8/feeds/contacts/default/full/9dfe9ff09a3a756')
