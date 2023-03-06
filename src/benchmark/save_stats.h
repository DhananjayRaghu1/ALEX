#include <iostream>
#include <fstream>

class StatsWriterCSV;

inline static StatsWriterCSV &end_row(StatsWriterCSV &file);
inline static StatsWriterCSV &flush(StatsWriterCSV &file);

class StatsWriterCSV
{
  std::ofstream fs_;
  const std::string separator_;

public:
  StatsWriterCSV(const std::string filename, const std::string separator = ",")
      : fs_(), separator_(separator)
  {
    fs_.exceptions(std::ios::failbit | std::ios::badbit);
    fs_.open(filename);
  }

  ~StatsWriterCSV()
  {
    flush();
    fs_.close();
  }

  void flush()
  {
    fs_.flush();
  }

  void end_row()
  {
    fs_ << std::endl;
  }

  StatsWriterCSV &operator<<(StatsWriterCSV &(*val)(StatsWriterCSV &))
  {
    return val(*this);
  }

  StatsWriterCSV &operator<<(const char *val)
  {
    fs_ << '"' << val << '"' << separator_;
    return *this;
  }

  StatsWriterCSV &operator<<(const std::string &val)
  {
    fs_ << '"' << val << '"' << separator_;
    return *this;
  }

  template <typename T>
  StatsWriterCSV &operator<<(const T &val)
  {
    fs_ << val << separator_;
    return *this;
  }
};

inline static StatsWriterCSV &end_row(StatsWriterCSV &file)
{
  file.end_row();
  return file;
}

inline static StatsWriterCSV &flush(StatsWriterCSV &file)
{
  file.flush();
  return file;
}
