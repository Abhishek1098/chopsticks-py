
// Make a simple model
class NeuralNetwork
{
  // initialize network here
  constructor()
  {
    this.network = [new Layer(0,0,true), new Layer(4,4,false), new Layer(4,5,false)];
  }
  // 4, 4, 5 nodes in respective layers

  //feed forward - calculate move
  feedForward()
  {
    //loop through each layer
    //j is the layer you are in
    for (var j = 1; j < network.length; j++)
    {
      // multiply prev layer's activations by weights
      network[j].activation_values = network[j].weights.multiply(network[j-1].activation_values);
      network[j].activation_values = relu(network[j].activation_values)
      for (var i =0 ; i < network[j].activation_values.length; i++)
      {
        console.log(etwork[j].activation_values[i]);
      }
    }
  }

  relu(activation_values)
  {
    for (var i = 0; i < activation_values.length; i++)
    {
      activation_values[i] = x;
      if (x < -10) {
        activation_values[i] = 0;
      } else if (x > 10) {
        activation_values[i] = 1;
      } else {
        activation_values[i] = 1 / (1 + Math.exp(-x));
      }
    }
  }
}

class Layer
{
  
  constructor(nodesPrevLayer,nodesThisLayer, isFirstLayer)
  {
    this.activation_values = [];
    if (isFirstLayer == true)
    {
      activation_values = [2, 3, 4, 1];
    } else {
      weights = new Matrix(nodesPrevLayer,nodesThisLayer);
      weights.generate();
    }
  }
  
}

class Matrix
{
  constructor (rows, cols)
  {
    // var m =  new Matrix(2,3)
    this.rows = rows;
    this.cols = cols;
    this.matrix = [];

    for (var i = 0; i < this.rows; i++)
    {
      this.matrix[i] = [];
      for (var j = 0; j < this.cols; j++)
      {
        this.matrix[i][j] = 0;
      }
    }
  }

  print()
  {
    for (var i = 0; i < this.rows; i++)
    {
      for (var j = 0; j < this.cols; j++)
      {
        console.log(this.matrix[i][j]);
      }
      console.log()
    }
  }

  generate()
  {
    for (var i = 0; i < this.rows; i++)
    {
      for (var j = 0; j < this.cols; j++)
      {
        this.matrix[i][j] = Math.random();
      }
    }
  }

  mutate()
  {
    var i = Math.floor(Math.random() * this.rows);
    var j = Math.floor(Math.random() * this.cols);
    this.matrix[i][j] = Math.random()*10;  
  }

  multiply(n)
  {
    let result = new Matrix(this.rows, n.cols)
    for (let i = 0; i < result.rows; i++)
    {
      let a = this;
      let b = n;

      for (let j = 0; j < result.cols; j++)
      {
        for (var k = 0; k < a.cols; k++)
        {
          result.matrix[i][j] += a.matrix[i][k] * b.matrix[k][j];
        }
      }
    }
    return result;
  }
}

nn = new NeuralNetwork();
nn.feedForward();


     