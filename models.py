# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)

class pos_config(models.Model):
	_inherit = 'pos.config'

	point_of_sale = fields.Integer('Point of Sale')

class pos_order(models.Model):
	_inherit = 'pos.order'

	rev = fields.Char('CouchDB Rev',readonly=1)
