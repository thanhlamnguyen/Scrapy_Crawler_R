import scrapy

import scrapy
import re
from ..items import EbayItem


class EbaSpider(scrapy.Spider):
    name = 'eba'
    allowed_domains = ['ebay.com']
    start_urls = ['https://www.ebay.com/p/17033751250?iid=193883678249']
                 
                  
    def parse(self, response):
        #<h1 class="product-title">Samsung Galaxy Note10 SM-N970U - 256GB - Aura Black (Unlocked) (Single SIM)</h1>
        name_product = response.xpath('//h1[@class="product-title"]/text()').get()
        #<div class="display-price">9,042,727.27 VND</div>
        price = response.xpath('//div[@ class="display-price"]/text()').get()
        #<span class="star--rating" tabindex="-1" aria-hidden="true"><i class="fullStar"></i><i class="fullStar"></i><i class="fullStar"></i><i class="fullStar"></i><i class="midStar"></i></span>
        rating= response.xpath('//span[@class="star--rating"]/text()').get()
        # <div id="ProductDetails" class="product-description card collapsed"><div><h2 class="box-title">About this product</h2><div class="description" tabindex="-1" aria-hidden="true"><section class="product-spectification"><div class="spec-row"><h2>Product Identifiers</h2><ul><li class=""><div class="s-name">Brand</div><div class="s-value">Samsung</div></li><li class=""><div class="s-name">MPN</div><div class="s-value">SMN970U1, SM-N970UZKAXAA, SMN970UZSAATT, SMN970U, SMN970UZWAVZW, SMN970UZKAATT, SMN970UZSATMB, SMN970UZWATMB, SMN970UZSAXAA, SMN970UZKATMB, SMN970UZSAVZW, SMN970UZWAATT, SMN970UZKAXAA, SMN970UZKAVZW</div></li><li class=""><div class="s-name">GTIN</div><div class="s-value">0680168902967</div></li><li class=""><div class="s-name">UPC</div><div class="s-value">0887276352831, 0680168902967</div></li><li class=""><div class="s-name">Model</div><div class="s-value">Samsung Galaxy Note10</div></li><li class=""><div class="s-name">eBay Product ID (ePID)</div><div class="s-value">17033751250</div></li></ul></div><div class="spec-row"><h2>Product Key Features</h2><ul><li class=""><div class="s-name">SIM Card Slot</div><div class="s-value">Single SIM</div></li><li class=""><div class="s-name">Network</div><div class="s-value">Unlocked</div></li><li class=""><div class="s-name">Operating System</div><div class="s-value">Android</div></li><li class=""><div class="s-name">Storage Capacity</div><div class="s-value">256 GB</div></li><li class=""><div class="s-name">Color</div><div class="s-value">Black</div></li><li class=""><div class="s-name">Connectivity</div><div class="s-value">USB Type-C, NFC, LTE</div></li><li class=""><div class="s-name">Processor</div><div class="s-value">Octa Core</div></li><li class=""><div class="s-name">Style</div><div class="s-value">Bar</div></li><li class=""><div class="s-name">Features</div><div class="s-value">Facial Recognition, Wireless PowerShare, AMOLED Display, HDR10+, Fast Wireless Charging, Ultra Wide-Angle Camera, Infinity-O Display, Telephoto Lens, Triple Rear Camera, Super Fast Charging, Ultrasonic Fingerprint Sensor</div></li><li class=""><div class="s-name">Camera Resolution</div><div class="s-value">16.0 MP</div></li><li class=""><div class="s-name">Screen Size</div><div class="s-value">6.3 in</div></li><li class=""><div class="s-name">RAM</div><div class="s-value">8 GB</div></li></ul></div><div class="spec-row"><h2>Additional Product Features</h2><ul><li class=""><div class="s-name">Brand Color</div><div class="s-value">Aura Black</div></li><li class=""><div class="s-name">Manufacturer Color</div><div class="s-value">Aura Black</div></li><li class=""><div class="s-name">Model Number</div><div class="s-value">Sm-N970u</div></li></ul></div></section></div></div><div class="product-details__see-more"><button class="btn btn--fluid p-more new-ui" data-tracking="[{&quot;eventFamily&quot;:&quot;PRP&quot;,&quot;eventAction&quot;:&quot;ACTN&quot;,&quot;actionKind&quot;:&quot;EXPAND&quot;,&quot;operationId&quot;:&quot;2349526&quot;,&quot;flushImmediately&quot;:false,&quot;eventProperty&quot;:{&quot;parentrq&quot;:&quot;750ad55017c0a9fc313fffd2ffff9db8&quot;,&quot;pageci&quot;:&quot;8850a057-d1b5-4ee9-93a4-a0bebb30b632&quot;,&quot;moduledtl&quot;:&quot;mi:3875|li:7704&quot;}},{&quot;actionKind&quot;:&quot;EXPAND&quot;}]" aria-label="Show more product details"><a id="">Show More</a><span class="icon-chevron-down new-ui"></span></button><button class="btn btn--fluid p-less new-ui" data-tracking="[{&quot;eventFamily&quot;:&quot;PRP&quot;,&quot;eventAction&quot;:&quot;ACTN&quot;,&quot;actionKind&quot;:&quot;COLLAPSE&quot;,&quot;operationId&quot;:&quot;2349526&quot;,&quot;flushImmediately&quot;:false,&quot;eventProperty&quot;:{&quot;parentrq&quot;:&quot;750ad55017c0a9fc313fffd2ffff9db8&quot;,&quot;pageci&quot;:&quot;8850a057-d1b5-4ee9-93a4-a0bebb30b632&quot;,&quot;moduledtl&quot;:&quot;mi:3875|li:7705&quot;}},{&quot;actionKind&quot;:&quot;COLLAPSE&quot;}]" aria-label="Show less product details"><a id="">Show Less</a><span class="icon-chevron-up new-ui"></span></button></div></div>
        information = response.xpath('//div[@class="product-description card collapsed"]/text()').get()
        item = EbayItem()
        item["name_product"] = name_product
        item["price"] = price
        item["rating"] = rating
        item["information"] = information
        yield item
        pass
