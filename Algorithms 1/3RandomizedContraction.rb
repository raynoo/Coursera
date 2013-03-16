#Implementation of Karger's Algorithm to find min-cut of a graph
class Mincut
  @adj_list
  
  def initialize
    @adj_list = Hash.new
    File.open('3input.txt', 'r').each_line do |line|
      nodes = line.chomp.split(/[\s\t]/).map { |x| x.to_i }
      @adj_list[nodes[0]] = nodes.slice(1..(-1))
    end
  end
  
  def contract
    random = Random.new()
    i = 0
    iterations = @adj_list.size()
    
    while (@adj_list.keys().size > 2 and i < iterations) do
      node_u = random.rand(iterations)
      if @adj_list.include?(node_u)
        adj_size = @adj_list[node_u].size
        node_v = @adj_list[node_u][random.rand(adj_size)]
        
#        puts "\n"
#        p "u: " + node_u.to_s + " v: " + node_v.to_s
#        p "node list u: " + @adj_list[node_u].sort.to_s()
        
        if @adj_list.has_key?(node_v)
#          p "node list v: " + @adj_list[node_v].to_s()

          #merge lists of u and v (shouldn't be unique set)
          @adj_list[node_u] += @adj_list[node_v]
          #delete duplicate entries of u and v in merged list
          @adj_list[node_u].delete(node_v)
          @adj_list[node_u].delete(node_u)
#          p "node list u: " + @adj_list[node_u].to_s()

          #for each in merged list, add an edge back to u 
          #from their adjacency lists
          @adj_list[node_u].each do |i|
            @adj_list[i] += [node_u]
          end
          #delete u and v once, since it would have been 
          #added twice above
          @adj_list[node_u].each do |i|
            @adj_list[i].delete(node_v)
            @adj_list[i].delete(node_u)
          end
          #remove node v from graph since its contracted into u
          @adj_list.delete(node_v)
        end
        i += 1
      end
    end
    #mincut = number of edges in last 2 nodes
    @adj_list.values[0].size
  end
end

if __FILE__ == $0
  min = 9999
  50.times do
    i = Mincut.new.contract()
    min = i if min > i
  end
  p "Min-Cut: " + min.to_s
end