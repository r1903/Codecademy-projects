using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int xCoordinate, out int yCoordinate){
      switch (key)
      {
        case "LeftArrow":
          xCoordinate = -1;
          yCoordinate = 0;
          break;
        case "RightArrow":
          xCoordinate = 1;
          yCoordinate = 0;
          break;
        case "UpArrow":
          xCoordinate = 0;
          yCoordinate = -1;
          break;
        case "DownArrow":
          xCoordinate = 0;
          yCoordinate = 1;
          break;
        default:
        	xCoordinate = 0;
          yCoordinate = 0;
          break;
      }
    }

    public new static char UpdateCursor(string key){
      switch (key)
      {
        case "LeftArrow":
          return '<';
        case "RightArrow":
          return '>';
        case "UpArrow":
          return '^';
        case "DownArrow":
          return 'v';
        default:
          return '<';
      }
    }
    public new static int KeepInBounds(int coordinate, int maxvalue)
    {
      if (coordinate < 0)
      {
        return 0;
      }
      else if (coordinate >= maxvalue)
      {
        return maxvalue - 1;
      }
      else 
      {
        return coordinate;
      }
    }

    public new static bool DidScore(int x1, int y1, int x2, int y2)
    {
      if (x1 == x2 && y1 == y2)
      {
        return true;
      }
      else
      {
        return false;
      }
    }
  }
}