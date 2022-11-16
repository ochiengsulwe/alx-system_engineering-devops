#!/usr/bin/env ruby

puts ARGV[0].scan(\b/School/g\b).join
