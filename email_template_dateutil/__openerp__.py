# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Email Template Date Utils',
    'version': '0.1',
    'author': "Savoir-faire Linux,Odoo Community Association (OCA)",
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Others',
    'summary': 'Adds extra date functions for email templates',
    'description': """
This module adds an extra filter in email templates:

format_date(format, tz=tzname, lc=locale)
    : parses and formats a date or datetime string.
    Optional parameter tz allows specifying the timezone to use. Otherwise, the
    user's timezone or server timezone will be used. If none are found, time is
    left in UTC.
    Optional parameter lc allows specifying the locale to use.
    If none are found, locale is left in en_US

Example: ${ object.date_field|format_date('%m/%d/%Y') }


Contributors
------------
* Vincent Vinet (vincent.vinet@savoirfairelinux.com)
""",
    'depends': [
        'email_template',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
