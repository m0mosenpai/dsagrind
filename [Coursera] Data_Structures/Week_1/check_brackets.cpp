#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']') {
            // std::cout <<"Matches with " << type << std::endl;
            return true;
        }
        if (type == '{' && c == '}') {
            // std::cout <<"Matches with " << type << std::endl;
            return true;
        }
        if (type == '(' && c == ')') {
            // std::cout <<"Matches with " << type << std::endl;
            return true;
        }
        // std::cout << "Doesn't match with any bracket" << std::endl;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    getline(std::cin, text);

    std::stack <Bracket> opening_brackets_stack;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];
        // std::cout << "Current: " << next << std::endl;

        if (next == '(' || next == '[' || next == '{') {
            // std::cout << "It's an opening bracket! Adding to stack." << std::endl;
            opening_brackets_stack.emplace(Bracket(next, position));
        }

        if (next == ')' || next == ']' || next == '}') {
            if (opening_brackets_stack.empty()){
                std::cout << position + 1 << std::endl;
                return 0;
            }
            // std::cout << "It's a closing bracket!" << std::endl;
            Bracket bracketObj = opening_brackets_stack.top();
            // std::cout << "bracketObj Type: " << bracketObj.type << " Position: " << bracketObj.position + 1 << std::endl;
            if (!bracketObj.Matchc(next)){
                std::cout << position + 1 << std::endl;
                return 0;
            }
            opening_brackets_stack.pop(); 
            // std::cout << "Popped off stack" << std::endl;
        }
    }
    if (!opening_brackets_stack.empty()) {
        // std::cout << "Stack is not empty!" << std::endl;
        std::cout << opening_brackets_stack.top().position + 1 << std::endl;
        return 0;
    }

    std::cout << "Success" << std::endl;
    return 0;
}
