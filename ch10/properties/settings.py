# Scrapy settings for properties project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'properties'

SPIDER_MODULES = ['properties.spiders']
NEWSPIDER_MODULE = 'properties.spiders'

ITEM_PIPELINES = {
    'properties.pipelines.PricePipeline': 100, 
    'properties.geopipeline.GeocodingPipeline': 200,
}

# Crawl responsibly by identifying yourself (and your website)
# on the user-agent
#USER_AGENT = 'properties (+http://www.yourdomain.com)'

EXTENSIONS = {
    'properties.distextension.BatchToScrapyd': 500,
    'properties.distextension.MongoImportOnFinish': 500
}

DIST_MONGO_DB = 'properties'
DIST_MONGO_COLLECTION = 'properties'

HTTPCACHE_ENABLED = True

ENABLE_IMAGES = False
if ENABLE_IMAGES:
    import os
    ITEM_PIPELINES['scrapy.contrib.pipeline.images.ImagesPipeline'] = 1
    IMAGES_STORE = os.path.join(os.getcwd(), 'images')
    if not os.path.exists(IMAGES_STORE):
        os.makedirs(IMAGES_STORE)

