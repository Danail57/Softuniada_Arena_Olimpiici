#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


long long int diff(long long n, long long p, long long stations[3])
{

   // long long dist, dist2, dist3;
   long long dist = min(abs(p - stations[0]), n - abs(p - stations[0]));
   long long dist2 = min(abs(p - stations[1]), n - abs(p - stations[1]));
   long long dist3 = min(abs(p - stations[2]), n - abs(p - stations[2]));

   long long distances[] = { dist, dist2, dist3 };
   long long nearest_dist_to_station = n;

   for (auto d : distances)
   {
      if (d < nearest_dist_to_station)
      {
         nearest_dist_to_station = d;
      }
   }

   return abs(nearest_dist_to_station);
}

int main()
{
   long long n, p;
   cin >> n >> p;

   long long stations[3];

   for (int i = 0; i < 3; i++)
   {
      cin >> stations[i];
   }
   cout << diff(n, p, stations) <<endl;
}
