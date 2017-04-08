# The software is released under MIT License.
#
# Copyright 2017 github.com/ptrk01
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software # without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A #PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import sqlite3 as lite
import sys

'''
Since Byteball software does not provide an API yet to request the underlying database,
this peace of software offers functions to return data from the database in Json format.

Only a few tables are already implemented. However it can be extended very easily by using the
database reference of Byteball (see link below)

Reference of database schema
https://github.com/byteball/byteballcore/blob/master/byteball-sqlite.sql
'''

class Api:
    con = None
    def __init__(self):
        try:
            '''
            Locations of Byteball's sqlite database
            MacOS: /Users/<USER>/Library/Application Support/byteball/byteball-light.sqlite
            Linux: ~/.config/byteball/byteball-light.sqlite
            Windows: %LOCALAPPDATA%\byteball/byteball-light.sqlite
            '''
            db_path = "/Users/pat/Library/Application Support/byteball/byteball-light.sqlite"
            self.con = lite.connect(db_path)
            self.con.row_factory = lite.Row
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)

    def getAddresses(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM addresses')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getAddress(self, address):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM addresses WHERE address = "%s"' % (address))
        return [ dict(rec) for rec in cur.fetchall() ]

    def getWallets(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM wallets')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getBalls(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM balls')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getBall(self, ball):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM balls WHERE ball = "%s"' % (ball))
        return [ dict(rec) for rec in cur.fetchall() ]

    def getUnitWitnesses(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM unit_witnesses')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getMessages(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM messages')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getMessagesByApp(self, app):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM messages WHERE app = "%s"' % (app))
        return [ dict(rec) for rec in cur.fetchall() ]

    def getSpentProofs(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM spend_proofs')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getInputPayments(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM inputs')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getOutputPayments(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM outputs')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getPeers(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM peers')
        return [ dict(rec) for rec in cur.fetchall() ]

    def getSharedAddresses(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM shared_addresses')
        return [ dict(rec) for rec in cur.fetchall() ]

    def close(self):
        self.con.close()
