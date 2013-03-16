#Implementation of Dijkstra's single-source shortest-path algorithm
class Dijkstras

  def readInput
    @adj_list = Hash.new
    File.open('5input.txt', 'r').each_line do |line|
      nodes = line.chomp.split(/[\s\t]/)
      
      list = Hash.new; 
      node = nodes[0].to_i
      
      nodes.slice(1..(-1)).each { |x|
        list[x.split(/,/)[0].to_i] = x.split(/,/)[1].to_i
      }
      list.delete(0)
      @adj_list[node] = list
      
    end
    dijkstra
  end

  def dijkstra
    @A = FakingHeap.new
    @A.add 1, 0
    
    node = 1
    @X = [1]
    
    until @X.size == @adj_list.size
      @adj_list[node].each { |neighbor|
        if(@A.get(neighbor[0]).nil? or @A.get(neighbor[0]) > (@A.get(node) + neighbor[1]))
          @A.add(neighbor[0], @A.get(node) + neighbor[1])
        end
      }
      node = @A.get_min(@X) if @A.size > 1
      @X += [node]
#      p @X
    end
    p @A.get(7), @A.get(37), @A.get(59), @A.get(82), @A.get(99), @A.get(115), @A.get(133), @A.get(165), @A.get(188), @A.get(197)
  end
  
end

class FakingHeap
  
  def initialize
    @list = Hash.new
  end
  
  def add node, weight
    @list[node] = weight
  end
  
  def get node
    @list[node]
  end
  
  def get_min listX
    min = -1
    @list.sort_by{ |node, avalue| avalue }.each{ |x,y| 
      if !listX.include?(x)
        min=x
        break
      end
      
      }
    min
  end
  
  def size
    @list.size()
  end
  
  def sorted
    @list.sort_by{ |node, avalue| node }
  end
end

if __FILE__ == $0
  Dijkstras.new().readInput()
end