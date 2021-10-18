# frozen_string_literal: true

n = ARGV[0].to_i

fizzbuzz = 0
fizz = 0
buzz = 0
none = 0

# start_time = Time.now
Range.new(1, n).each do |i|
  if (i % 15).zero?
    fizzbuzz += 1
  elsif (i % 3).zero?
    fizz += 1
  elsif (i % 5).zero?
    buzz += 1
  else
    none += 1
  end
end

# p "elapsed_time:#{Time.now - start_time}[sec]"
p "fizzbuzz:#{fizzbuzz}"
p "fizz:#{fizz}"
p "buzz:#{buzz}"
p "none:#{none}"
