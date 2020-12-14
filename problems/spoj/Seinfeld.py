# Approach for the problem is similar to MMASS and the solution to this problem is here. Problem can be solved by using a stack. Steps involved are:-
# 1.) If s[i] is '{' then push it in stack.
# 2.) If s[i] is '}' then there are two conditions, if top of stack is '{' then pop the stack else if stack is empty or top of stack is '}' then push s[i] in stack.
# 3.) Count the number of '{' and '}' remaining in stack, let it be s1 and s2.
#   if s1 and s2 are even, then answer would be (s1+s2)/2.
#   else it would be (s1+s2)/2+1.

# CODE:

# #include <bits/stdc++.h>
# using namespace std;
# int main()
# {
#     int r=0;
#     while(1)
#     {r++;
#         string s;
#         cin>>s;
#         if(s[0]=='-')
#         break;
#         stack <char> st;
#         int i,j,k,l=s.size();
#         for(i=0;i<l;i++)
#         {
#             if(s[i]=='{')
#             st.push(s[i]);
#             else
#             {
#                 if(st.size())
#                 {
#                     if(st.top()=='{')
#                     {
#                         st.pop();
#                     }
#                     else
#                     st.push(s[i]);
#                 }
#                 else
#                 st.push(s[i]);
#             }
#         }
#         int s1=0,s2=0;
#         while(st.size())
#         {
#             if(st.top()=='}')
#             s2++;
#             else
#             s1++;
#             st.pop();
#         }
#         if(s1&&s2&&s1%2)
#         {
#             printf("%d. %d\n",r,(s1+s2)/2+1);
#         }
#         else
#         {
#             printf("%d. %d\n",r,(s1+s2)/2);
#         }
#     }
#     return 0;

# }
