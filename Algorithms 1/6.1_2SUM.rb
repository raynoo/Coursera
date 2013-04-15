#Implementation of 2-SUM algorithm using a hash set.
#Compute number of target sums in an interval a1..a2 for which
# there's a distinct x,y in input such that x+y=target.

require 'set'

def init
  @input = Set.new
  File.open('6input2.txt', 'r').each_line do |line|
    @input.add(line.to_i);
  end
  @targets = Array.new
end

def two_sum
#  a1 = 60; a2 = 100 #6test1_1.txt => 28
  a1 = 2500; a2 = 4000
  (a1..a2).each { |t|
    @input.each { |x|
      if x != t-x and @input.include?(t-x)
        @targets.push t
        break
      end
    }
  }
end

init
two_sum
p @targets.size