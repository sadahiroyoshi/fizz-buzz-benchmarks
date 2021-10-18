# frozen_string_literal: true

n = ARGV[0].to_i

# start_time = Time.now
Range.new(1, n).each do |i|
  if (i % 15).zero?
    print "fizzbuzz\n"
  elsif (i % 3).zero?
    print "fizz\n"
  elsif (i % 5).zero?
    print "buzz\n"
  else
    print "#{i}\n"
  end
end

# p "elapsed_time:#{Time.now - start_time}[sec]"
