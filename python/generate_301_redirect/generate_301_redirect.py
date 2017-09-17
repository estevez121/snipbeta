# -*- encoding: utf-8 -*-
#
# Gate39Media Python Script for Generate 301 Redirect.
# Author: Eduardo Estevez <eestevez@gate39media.com>
# Last Updated: 03/01/2016
# @version
# @package
# @subpackage
# @copyright
# @license
#
#!/usr/bin/env python

"""
INSERT INTO `wp_WP_SEO_Redirection` ( `enabled`, `redirect_from`, `redirect_from_type`, `redirect_from_folder_settings`, `redirect_from_subfolders`, `redirect_to`, `redirect_to_type`, `redirect_to_folder_settings`, `regex`, `redirect_type`, `url_type`, `postID`) VALUES ( 1, 'http://www.dormantrading.com/aboutus/contactus1.aspx', 'Page', 0, 0, '/contact-us/', 'Page', 0, '', '301', 1, NULL)
"""

try:

  fhand = open( 'sitemap.csv' )

  sql_content = ''

  #Count Links
  links_count = dict()

  for line in fhand:

      line_str = line.strip()
      line_links = line_str.split(',')

      link = line_links[0]
      link = link.lower()

      links_count[ link ] = links_count.get( link ,0) + 1

      sql_content = sql_content + "INSERT INTO `wp_WP_SEO_Redirection` ( `enabled`, `redirect_from`, `redirect_from_type`, " \
                                  "`redirect_from_folder_settings`, `redirect_from_subfolders`, `redirect_to`, `redirect_to_type`, " \
                                  "`redirect_to_folder_settings`, `regex`, `redirect_type`, `url_type`, `postID`) " \
                                  "VALUES ( 1, '"+line_links[0]+"', 'Page', 0, 0, " \
                                  "'"+line_links[1]+"', 'Page', 0, '', '301', 1, NULL);\n"



  #for link,counts in links_count.items():

  #    print link,':',counts


  print sql_content

  #Generate SQL
  sql_file = open('sitemap.sql', 'w')

  sql_file.write(sql_content)
  sql_file.close()

except:
  print "File can not open"
  exit()