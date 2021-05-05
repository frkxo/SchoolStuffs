#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void cocktail_sort(int arr[], int n);
void print_array(int arr[], int size);
void swap_int(int& x, int& y);

int main(){
    int arr[] = {2, 5, 6, 1, 12 ,88, 95, 31};
    int n = sizeof(arr) / sizeof(arr[0]);
    cocktail_sort(arr,n);
    cout << "Our array is: \n";
    print_array(arr, n);
    return 0;

}

void cocktail_sort(int arr[], int n){
    bool swap = true;
    int start = 0, end = n - 1;

    while (swap){
        swap = false;
        for(int i = start;i < end;i++){//This code block is scaning the array from left to right with buble sort algorithm.
            if(arr[i] > arr[i + 1]){
                swap_int(arr[i], arr[i + 1]);
                swap = true;
            }
        }
        if(!swap){
            break;
        }
        swap = false;
        end--;
        for(int i = end - 1;i >= start;i--){//This code block is scaning the array from right to left with buble sort algorithm.
            if(arr[i] > arr[i + 1]){
                swap_int(arr[i], arr[i + 1]);
                swap = true;
            }
        }
        start++;
    }
}

void print_array(int arr[], int size){
    for(int i = 0;i < size;i++){
        cout << arr[i] << " ";
    }
}

void swap_int(int& x, int& y){
    int temp = x;
    x = y;
    y = temp;
}
