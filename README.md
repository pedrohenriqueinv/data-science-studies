/* sort_int.c – quick‑sort implementation for an integer array */

  #include <stddef.h>

  /**  - Sorts an array of integers in ascending order using the quicksort algorithm.
  - @param arr  Pointer to the first element of the array.  - @param n    Number of elements in the array.
   */
  void sort_int_array(int *arr, size_t n) {
   if (arr == NULL || n < 2) {
   return;
   }

  -  /* Helper to swap two integers */
   static void swap(int *a, int *b) {
   int tmp = *a;
   *a = *b;
   *b = tmp;
   }

  -  /* Recursive quicksort working on pointers */
   static void quicksort(int *low, int *high) {
   if (low >= high) {
       return;
   }
   int *pivot = low;
   int *left  = low + 1;
   int *right = high;

   while (left <= right) {
       while (left <= right && *left <= *pivot) {
           ++left;
       }
       while (left <= right && *right >= *pivot) {
           --right;
       }
       if (left < right) {
           swap(left, right);
           ++left;
           --right;
       }
   }
   swap(pivot, right);
   quicksort(low, right - 1);
   quicksort(right + 1, high);
   }

  -  quicksort(arr, arr + n - 1);
  }