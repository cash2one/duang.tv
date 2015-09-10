#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2013 meiritugua.com

import time
from lib.query import Query

class Post_nodeModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "post_node"
        super(Post_nodeModel, self).__init__()

    def add_new_post_node(self, post_node_info):
        return self.data(post_node_info).add()