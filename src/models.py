import os
import logging
from datetime import datetime
from peewee import Model
from peewee import PrimaryKeyField as PrimaryKey
from peewee import TextField as Text
from peewee import Float
from peewee import Integer
from peewee import DateTimeFiels as DateTime

from playhouse.postgres_ext import ArrayField as Array
from playhouse.postgres_ext import JSONField as Json

basedir = os.path.abspath(os.path.dirname(__file__))


database_name = 'vulner.db'


database = peewee.SqliteDatabase(
    database_name,
    pragmas={
        'journal_mode': 'wal',
        'cache_size': -512 * 1024,
        'syncronous': 0,
        'foreign_keys': 1})


class Vulnerability(Model):
    class Meta:
        ordering = ("vulnerability_id", )
        table_name = "vulnerability"
        database = database

    # {INTEGER} Table Identifier
    id = PrimaryKey(null=False)

    # {STRING} Special internal ID
    vulnerability_id = Text(default="undefined")

    # {ARRAY} Vulnerability CVE IDs if exists
    cve_ids = Array(Text, default=[])

    # {ARRAY} Vulnerability CWE IDs if exists
    cwe_ids = Array(Text, default=[])

    # {ARRAY} Vulnerability NPM IDs if exists
    npm_ids = Array(Text, default=[])

    # {ARRAY} Vulnerability CAPEC IDs if exists
    capec_ids = Array(Text, default=[])

    # {ARRAY} Vulnerability MS IDs if exists
    ms_ids = Array(Text, default=[])

    # {ARRAY} Vulnerability D2SEC IDs if exists
    d2sec_ids = Array(Text, default=[])

    # {STRING} Vulnerability type (ex. cve, npm, ...)
    type = Text(default="undefined")
    # {STRING} Vulnerability source (URL)
    source = Text(default="undefined")


    # {STRING} Vulnerability title
    title = Text(default="undefined")
    # {STRING} Vulnerability description
    description = Text(default="undefined")
    # {STRING} Vulnerability recommendations
    recommendations = Text(default="undefined)

    # {STRING} Vulnerability versions
    vulnerable_versions = Text(default="")
    # {STRING} Vulnerability patched version
    patched_versions = Text(default="")

    # {ARRAY} Vulnerability references
    references = Array(Text, default=[])

    # {DATETIME} Vilnerability published date
    published = DateTime(default=datetime.utcnow)
    # {DATETIME} Vulnerability last modified data
    modified = DateTime(default=datetime.utcnow)
    # {DATETIME} Vulnerability CVSS time
    cvss_time = DateTime(default=datetime.utcnow)

    # {JSON} Vulnerability access parameter
    access = Json(default={"vector": "undefined", "complexity": "undefined", "authentication": "undefined"})
    # {JSON} Vulnerability impact parameter
    impact = Json(default={"confidentiality": "undefined", "integrity": "undefined", "availability": "undefined"})

    # {FLOAT} Vulnerability CVSS Score parameter
    cvss_score = Float(default=0.0)
    # {STRING} Vulnerability CVSS Vecror
    cvss_vector = Text(default="undefined")
    # {INTEGER} Vulnerability Integer parameted
    rank = Integer(default=0)


    def __repr__(self):
        return "[{}] - [{}]: {}".format(self.id, self.vulner_id, self.title)

    def __str__(self):
        return self.vulner_id

    def tojson(self):
        return dict(
            id=self.id,
            vulnerability_id=self.vulnerability_id,
            title=self.title,
            cve_ids=self.cve_ids,
            cwe_ids=self.cwe_ids,
            capec_ids=self.capec_ids,
            npm_ids=self.npm_ids,
            d2sec_ids=self.d2sec_ids,
            type=self.type,
            source=self.source,
            title=self.title,
            description=self.description,
            recommendations=self.recommendations,
            vulnerable_versions=self.vulnerable_versions,
            patched_versions=self.patched_versions,
            references=self.references,
            published=self.published,
            modified=self.modified,
            cvss_time=self.cvss_time,
            access=self.access,
            impact=self.impact,
            cvss_score=self.cvss_score,
            cvss_vector=self.cvss_vector,
            rank=self.rank
        )
