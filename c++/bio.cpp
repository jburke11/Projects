#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using std::back_inserter;
using std::cin;
using std::copy;
using std::cout;
using std::endl;
using std::find;
using std::fixed;
using std::istringstream;
using std::max;
using std::ostream_iterator;
using std::ostringstream;
using std::pow;
using std::reverse_copy;
using std::runtime_error;
using std::setprecision;
using std::string;
using std::to_string;
using std::transform;
using std::vector;
bool IsValidDNASequence(const std::string& input) {
  for (auto ch : input) {
    if ((ch != 'A') && (ch != 'T') && (ch != 'C') && (ch != 'G')) { // checks to make sure each letter is ATCG
      return false;
    } else {
      continue;
    }
  }
  return true;
}

void GetReverseComplementSequence(const std::string& input,
                                  std::string* const output) {
  string in = "";
  reverse_copy(input.begin(), input.end(), back_inserter(in)); // makes reverse string
  ostringstream oss;
  for (auto ch : in) {
    switch (ch) { // replaces bases to make reverse complement
      case 'A':
        oss << 'T';
        break;
      case 'T':
        oss << 'A';
        break;
      case 'C':
        oss << 'G';
        break;
      case 'G':
        oss << 'C';
        break;

      default:
        break;
    }
  }
  *output = oss.str(); // writes oss string to output 
}

string GetRNATranscript(const std::string& input) {
  string rev = "";
  GetReverseComplementSequence(input, &rev); // get reverse complement first 
  ostringstream oss;
  for (auto ch : rev) { // replaces T with U
    if (ch == 'T') {
      oss << 'U';
    } else {
      oss << ch;
    }
  }
  return oss.str();
}

std::vector<std::vector<std::string>> GetReadingFramesAsCodons(
    const std::string& input) {
  string reverse = GetRNATranscript(input); // gets rna transcript for original transcript
  string temp = "";
  GetReverseComplementSequence(input, &temp);    // get reverse of that 
  string rna = GetRNATranscript(temp);      // get rna transcript for the complement seq
  vector<vector<string>> result;    // makes vector of vector of strings for the result
  for (int i = 0; i < 3; i++) {     // cycles through the transcript by each reading frame
    vector<string> reading_frame;   //make vector to hold codons
    string read;
    copy((reverse.begin() + i), reverse.end(), back_inserter(read)); // make the reading frame
    int codons = read.size() / 3; // find out how many codons there are 
    for (int j = 0; j < codons; j++) {
      string codon = "";
      int pos = j * 3;
      copy((read.begin() + pos), (read.begin() + (pos + 3)), // copy codons into a vector and increment the position by 3
           back_inserter(codon));
      reading_frame.push_back(codon);
    }
    result.push_back(reading_frame); // pushback the vector of codons into the result vector
  }
  for (int i = 0; i < 3; i++) {     //same process but for reverse seq
    vector<string> reading_frame;
    string read;
    copy((rna.begin() + i), rna.end(), back_inserter(read));
    int codons = read.size() / 3;
    for (int j = 0; j < codons; j++) {
      string codon = "";
      int pos = j * 3;
      copy((read.begin() + pos), (read.begin() + (pos + 3)),
           back_inserter(codon));
      reading_frame.push_back(codon);
    }
    result.push_back(reading_frame);
  }
  return result;
}

std::string Translate(const std::vector<std::string>& codon_sequence) {
  ostringstream oss;
  vector<string> codons = {
      "GCU", "GCC", "GCA", "GCG", "CGU", "CGC", "CGA", "CGG", "AGA", "AGG",
      "AAU", "AAC", "GAU", "GAC", "UGU", "UGC", "CAA", "CAG", "GAA", "GAG",
      "GGU", "GGC", "GGA", "GGG", "CAU", "CAC", "AUU", "AUC", "AUA", "UUA",
      "UUG", "CUU", "CUC", "CUA", "CUG", "AAA", "AAG", "AUG", "UUU", "UUC",
      "CCU", "CCC", "CCA", "CCG", "UCU", "UCC", "UCA", "UCG", "AGU", "AGC",
      "ACU", "ACC", "ACA", "ACG", "UGG", "UAU", "UAC", "GUU", "GUC", "GUA",
      "GUG", "UAG", "UGA", "UAA"};
  vector<string> amino_acids = {
      "A", "A", "A", "A", "R", "R", "R", "R", "R", "R", "N", "N", "D",
      "D", "C", "C", "Q", "Q", "E", "E", "G", "G", "G", "G", "H", "H",
      "I", "I", "I", "L", "L", "L", "L", "L", "L", "K", "K", "M", "F",
      "F", "P", "P", "P", "P", "S", "S", "S", "S", "S", "S", "T", "T",
      "T", "T", "W", "Y", "Y", "V", "V", "V", "V", "*", "*", "*"};
  for (auto codon : codon_sequence) {
    auto seq = find(codons.begin(), codons.end(), codon); //finds the codon in the codon vector
    int pos = seq - codons.begin(); // finds the position of the codon
    auto acid = amino_acids[pos]; // get the corresponding amino acid
    oss << acid; // write the acid to the ostringstream and return
  }
  return oss.str();
}

std::string GetLongestOpenReadingFrame(const std::string& DNA_sequence) {
  vector<vector<string>> reading_frames_as_codons =
      GetReadingFramesAsCodons(DNA_sequence);   // get the vector of vecotors of codons
  string max = "";
  for (auto vec : reading_frames_as_codons) { // iterate through each vector
    auto amino_seq = Translate(vec); // get the amino acid sequence
    for (auto start = amino_seq.begin(); start != amino_seq.end(); ++start) {   // cycle through amino acid seq
      auto begin = find(start, amino_seq.end(), 'M');   // find M
      auto end = find(start, amino_seq.end(), '*'); // find stop 
      string result = "";
      copy(begin, end + 1, back_inserter(result)); // copy the area between M and *
      if (result[result.length() - 1] != '*') { // if the end is not * skip it
        continue;
      }
      if (result.length() > max.length()) { // if the result is larger than the previous max, overwrite it
        max = result;
      } else {
        continue;
      }
    }
  }
  return max; // return the longest open reading frame
}