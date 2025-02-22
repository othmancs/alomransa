# -*- coding: utf-8 -*-
##############################################################################
#    Copyright (C) 2020 AtharvERP (<http://atharverp.com/>). All Rights Reserved
# Odoo Proprietary License v1.0
#
# This software and associated files (the "Software") may only be used (executed,
# modified, executed after modifications) if you have purchased a valid license
# from the authors, typically via Odoo Apps, atharverp.com or you have written agreement from
# author of this software owner.
#
# You may develop Odoo modules that use the Software as a library (typically
# by depending on it, importing it and using its resources), but without copying
# any source code or material from the Software. You may distribute those
# modules under the license of your choice, provided that this license is
# compatible with the terms of the Odoo Proprietary License (For example:
# LGPL, MIT, or proprietary licenses similar to this one).
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the Software
# or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
##############################################################################
{
    'name': "Remove Duplicate Product",
    'summary': """Clear duplicate products with single click""",
    'version': '16.0.0.1.0',
    'category': 'Contacts',
    'author': 'AtharvERP Business solution',
    'maintainer': 'AtharvERP Business solution',
    'contributors': ['Anil Kesariya <anil.r.kesariya@gmail.com>'],
    'website': 'http://atharverp.com',
    'live_test_url': 'http://atharverp.com/contactus',
    'depends': ['base_setup', 'sale'],
    'data': [
        'data/data.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/poster_image.gif'],
}
