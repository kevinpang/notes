# irb # Starts interactive ruby shell in unix

# Shows how to take in command line arguments (example of executing this file with arguments 1, 2, and 3: "ruby test.rb 1 2 3")
ARGV.each do |a|
  puts "Argument: #{a}"
end

# Functions
def sayGoodnight(name)
  "Goodnight #{name}"
end

puts sayGoodnight("Kevin")

def function_with_array_params(*args)
  puts args[0].to_s + args[1].to_s + args[2].to_s
end

function_with_array_params(1, 2, 3) # 123

# Arrays
a = [1, "cat", 3.14]
puts a[0]
puts a[1]
puts a[2]
puts a[-1] # 3.14
puts a[0, 2] # [1, "cat"]
puts a[0..2] # [1, "cat", 3.14]
a.push("dog")
puts a # 1, cat, 3.14, dog
a.shift # deletes the first item in the array
puts a # cat, 3.14, dog
a.pop # deletes the last item in the array
puts a # cat, 3.14
puts a.find { |item| item == "cat" } # cat
puts a.find { |item| item == "foo" } # nil
a.each { |item| puts item } # cat, 3.14
puts a.collect { |item| item.to_s + "foo" } # catfoo, 3.14foo
puts a.empty?
puts a.any? # Opposite of a.empty
a << "foo"
puts a # catfoo, 3.14foo, foo

b = []
c = Array.new

d = %w(ant bee cat dog elk) # Shortcut for making arrays of strings without having to enter in a lot of quotation marks
puts d[0]

# Hashes
instSection = {
  "cello"     => "string",
  "clarinet"  => "woodwind",
  "drum"      => "percussion",
  "oboe"      => "woodwind",
  "trumpet"   => "brass",
  "violin"    => "string",
  :foo        => "bar"
}

puts instSection["oboe"] # woodwind
puts instSection["cello"] # string
puts instSection["foo"] # nil
puts instSection[:foo] # bar

initialized_hash = Hash.new(0)
puts initialized_hash["foo"] # 0

another_way_to_create_a_hash = {}
another_way_to_create_a_hash["foo"] = "bar"
puts another_way_to_create_a_hash["foo"] # bar
puts another_way_to_create_a_hash["foo2"] # nil

# Hashes inside arrays (if you use arrows inside of an array, you'll end up with a Hash inside of that Array)
kitty_toys =
  [:shape => 'sock', :fabric => 'cashmere'] +
  [:shape => 'mouse', :fabric => 'calico'] +
  [:shape => 'eggroll', :fabric => 'chenille']

# So the above is equivalent to
kitty_toys = [
  {:shape => 'sock', :fabric => 'cashmere'},
  {:shape => 'mouse', :fabric => 'calico'},
  {:shape => 'eggroll', :fabric => 'chenille'}
]

kitty_toys.sort_by { |toy| toy[:fabric] }

# Regex
test_regex = /test/
puts "this is a test" =~ test_regex # Prints out the index of "test" (10)
puts "foo" =~ test_regex # nil
puts "this is a test test".sub(test_regex, "foo") # "this is a foo test" (Replaced first instance of "test" with "foo")
puts "this is a test test".gsub(test_regex, "foo") # "this is a foo foo" (Replaced all instances of "test" with "foo")

# Blocks
def callBlock
  yield # Invokes block
  yield # Invokes block again
end

callBlock { puts "In the block" }

callBlock do
  puts "In the block (declared another way)"
end

def callBlockWithArgument
  yield "foo" # Invokes block with "foo" as an argument
end

callBlockWithArgument { |arg| puts arg } # arg is the "block argument". We expect callBlockWithArgument to execute the code within the block and pass it one block argument here

callBlockWithArgument do |arg|
  puts arg
end

# class JukeboxButton < Button
#   def initialize(label, &action) # Ampersand signals second parameter will be a block
#     super(label)
#     @action = action
#   end
# 
#   def buttonPressed
#     @action.call(self) # Invokes block
#   end
# end
# 
# bStart = JukeboxButton.new("Start") { songList.start }
# bPause = JukeboxButton.new("Pause") { songList.pause }

# IO
print "This does not enter a newline after"
puts "This enters a newline after"
printf "Number: %5.2f, String: %s", 1.23, "hello" # Number:  1.23, String: hello
print "\n"

# Classes
class Song
  # Attribute shortcuts give public access to instance variables
  attr_reader :name, :artist, :duration # Declares accessor methods to instance variables @name, @artist, and @duration
  attr_writer :duration # Declares writable attribute to instance variable @duration
  #attr_accessor :duration # This is the same as declaring both attr_reader :duration and attr_writer :duration
  
  # Defines attributes that are allowed to be mass assigned
  #attr_accessible :duration
  
  @@plays = 0 # Class variable shared amongst all instances of the Song class
  
  # Constructor (called via Song.new)
  def initialize(name, artist, duration)
    # Instance variables
    @name = name
    @artist = artist
    @duration = duration
  end
  
  def to_s
    "Song: #{@name}--#{@artist} (#{@duration})"
  end
  
  # Long way of declaring accessor methods to instance variables (short way is to use attr_reader)
  # def name
  #   @name
  # end
  #   
  # def artist
  #   @artist
  # end
  #   
  # def duration
  #   @duration
  # end
  
  # Long way of declaring a writable attribute to be assigned to an instance variable (short way is to use attr_writer)
  # def duration=(newDuration)
  #   @duration = newDuration
  # end
  
  def play
    @@plays += 1
  end
  
  def Song.plays # Class method
    @@plays
  end
end

a_song = Song.new("Thriller", "Michael Jackson", 260)
puts a_song.inspect # <Song:0x1001346f0 @artist="Michael Jackson", @name="Thriller", @duration=260>
puts a_song.to_s # "Song: Thriller--Michael Jackson (260)"
puts a_song.name # "Thriller"
puts a_song.artist # "Michael Jackson"
puts a_song.duration # "260"
a_song.duration = 300
puts a_song.duration # "300"

a_song.play
b_song = Song.new("foo", "bar", 1)
b_song.play
puts Song.plays # "2"

class KaraokeSong < Song # KaraokeSong inherits from Song
  def initialize(name, artist, duration, lyrics)
    super(name, artist, duration) # Call parent class constructor
    @lyrics = lyrics
  end
  
  def to_s
    s = super # Calls to_s in parent class with the same arguments passed into this method (in this case there are no arguments)
    s + " [#{@lyrics}]"
  end
end
  
karaoke_song = KaraokeSong.new("My Way", "Frank Sinatra", 200, "I did it...myyyyyyyyyy way")
puts karaoke_song # "Song: My Way--Frank Sinatra (200) [I did it...myyyyyyyyyy way]"

# Singleton (note that this implementation is not thread-safe, if multiple threads were running it would be possible to create multiple Logger objects. Use
# the Singleton mixin provided by Ruby for thread-safe singletons)
class Logger
  private_class_method :new # Makes constructor private
  @@logger = nil
  
  def Logger.create
    @@logger = new unless @@logger # Use class variable @@logger if it already exists
    @@logger
  end
end

# Exception handling
begin
  raise SystemCallError, "test"
rescue SystemCallError => err
  puts "SystemCallError raised #{err}"
rescue StandardError
  puts "StandardError raised #{$!}" # When an exception is raised, Ruby places a reference to the Exception object in the global variable $! unless a name is specified (see how SystemCallError is handled)
ensure
  # Similar to a "Finally" block
  puts "Ensure fired"
end

# Modules are used for grouping methods, classes, and constants. They can be used for namespacing to prevent name clashes and for mixins.
module Trig
  def Trig.sin(x)
  end
  
  def Trig.cos(x)
  end
end

# Mixins
module Debug
  def whoAmI?
    "#{self.class.name} (\##{self.object_id}): #{self.to_s}"
  end
end

class Phonograph
  include Debug

  def initialize(name)
    @name = name
  end
  
  def to_s
    @name
  end
end

ph = Phonograph.new("West End Blues")
puts ph.whoAmI? # "Phonograph (#537766170): West End Blues"

# For loops
pages = %w(www.google.com, www.cnn.com, www.espn.com)

for page in pages
  puts page
end

pages.each { |page| puts page }

pages.each do |page|
  puts page
end

# HTTP
# require "net/http"

# http = Net::HTTP.new("www.google.com", 80)
# puts http.get("/", nil)

# Debugging
# ruby -r debug somefile.rb
# irb # IRB = "interactive ruby" is a Ruby shell where you can play around with Ruby in real time

# Useful functions
x = 5
puts x.class # Fixnum
puts x.respond_to? "to_s" # true
puts x.is_a? Object # true
puts x.kind_of? Object # true
puts x.instance_of? Object # false

variable = 5
Constant1 = 6 # Capital letter = constant

def foo(bar)
  puts bar
end

foo(:test) # Symbol, basically the same as a string
foo("test")

$global_variable

some_string = "str"
puts some_string.respond_to?(:length)

# Commented out since it prompts for input and creates files
# print "Type in your input: "
# input = gets # Prompt for user input
# puts "You typed #{input}"
# 
# code_words = {
#  'starmonkeys' => 'Phil and Pete, those prickly chancellors of the New Reich', 
#  'catapult' => 'chucky go-go', 
#  'firebomb' => 'Heat-Assisted Living', 
#  'Nigeria' => "Ny and Jerry's Dry Cleaning (with Donuts)",
#  'Put the kabosh on' => 'Put the cable box on'
# }
# 
# # Get evil idea and swap in code words
# print "Enter your new idea: " 
# idea = gets
# code_words.each do |real, code| 
#  idea.gsub!( real, code )
# end
# 
# # Save the jibberish to a new file
# print "File encoded.  Please enter a name for this idea: " 
# idea_name = gets.strip
# File::open( "idea-" + idea_name + ".txt", "w" ) do |f|
#  f << idea
# end

# Greed is a dice game where you roll up to five dice to accumulate
# points. The following "score" function will be used to calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
# number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice)
  h = Hash.new(0)
  dice.each { | d | h.store(d, h[d]+1) }
  
  score = 0
  
  score += h[1] * 100
  score += 700 if h[1] >= 3
  
  score += 200 if h[2] >= 3 
  score += 300 if h[3] >= 3
  score += 400 if h[4] >= 3
  
  score += h[5] * 50
  score += 350 if h[5] >= 3
  
  score += 600 if h[6] >= 3
  
  score
end

puts score([])
puts score([5])
puts score([1])
puts score([1,5,5,1])
puts score([2,3,4,6])
puts score([1,1,1])
puts score([2,2,2])
puts score([3,3,3])
puts score([4,4,4])
puts score([5,5,5])
puts score([6,6,6])
puts score([2,5,2,2,3])
puts score([5,5,5,5])