#include<bits/stdc++.h>

using namespace std;

typedef vector<int> vi;

#define pb push_back

const int numvars = 11500;
const int k = 10;
const double e = exp(1);
const int appearances = (int) (pow(2,k) / e / k);
const int clauses = numvars / 10 * 37; // replace 10 with k and 37 with appearances
vi ans[clauses];
int perm[clauses];

int main() {
	for (int i = 0; i < clauses; ++i) perm[i] = i;
	int curvar = 0;
	for (int i = 0; i < k; ++i) {
		for (int j = clauses - 1; j > 0; --j) {
			int idx = rand() % (j+1);
			swap(perm[j], perm[idx]);
		}
		for (int j = 0; j < clauses / appearances; ++j) {
			for (int of = 0; of < appearances; ++of) {
				ans[perm[j * appearances + of]].pb(curvar);
			}
			++curvar;
		}
	}
	printf("Number of variables:%d\n", curvar);
	for (int i = 0; i < clauses; ++i) {
		for (int j: ans[i]) {
			if (rand() & 1) printf("~");
			printf("%d ", j);
		}
		printf("\n");
	}

}

