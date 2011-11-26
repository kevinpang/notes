require 'twitter'
require 'twitter-text'

Twitter.configure do |config|
  config.consumer_key = '4EEUN3Cq2BpL3CHSHhT4A'
  config.consumer_secret = 'sPl7FuqjJPFahaSmIxEUsJKrzILhgZ0HPS3yICBfQ'
  
  # These will be unique per user, currently hardcoded to "KevinPang"'s Twitter account
  config.oauth_token = '14210167-vheY5nljQv0YiNx9vNvT6XuWTJXKhBYM3kuyUho'
  config.oauth_token_secret = 'LKe6yCNUaVgxse7A61wAo1SHvRc7TFo0RmNkCL5w'
end

url_tweets = Hash.new { |h, k| h[k] = [] } # {url, array of tweets containing the url}

# The Twitter API limits you to 200 tweets per request and 800 tweets total when querying a user's home timeline
(1..4).each do |i|
  Twitter.home_timeline(:count => 200, :page => i).each do |tweet|
    Twitter::Extractor.extract_urls(tweet.text) do |url|
      url_tweets[url] << tweet
    end
  end  
end

# Order by number of tweets containing the url (descending)
url_tweets = url_tweets.sort { |a, b| -(a[1].count <=> b[1].count) }

url_tweets.each do |url, tweets|
  puts "#{url} appears #{tweets.count} time#{'s' if tweets.count > 1}"
  
  tweets.each do |tweet|
    puts "#{tweet.user.screen_name}: #{tweet.text}"
  end
  
  puts ''
end