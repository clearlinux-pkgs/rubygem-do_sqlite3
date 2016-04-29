#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-do_sqlite3
Version  : 0.10.17
Release  : 6
URL      : https://rubygems.org/downloads/do_sqlite3-0.10.17.gem
Source0  : https://rubygems.org/downloads/do_sqlite3-0.10.17.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-do_sqlite3-lib
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-data_objects
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : sqlite-autoconf-dev

%description
# do_sqlite3
* <http://dataobjects.info>
## Description
A SQLite3 driver for DataObjects.

%package lib
Summary: lib components for the rubygem-do_sqlite3 package.
Group: Libraries

%description lib
lib components for the rubygem-do_sqlite3 package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n do_sqlite3-0.10.17
gem spec %{SOURCE0} -l --ruby > rubygem-do_sqlite3.gemspec

%build
gem build rubygem-do_sqlite3.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
do_sqlite3-0.10.17.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/do_sqlite3-0.10.17
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/do_sqlite3-0.10.17.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/do_sqlite3-0.10.17/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/do_sqlite3-0.10.17/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/do_sqlite3-0.10.17/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ChangeLog.markdown
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/README.markdown
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/.RUBYARCHDIR.-.do_sqlite3.time
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/compat.h
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_common.c
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_common.h
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_common.o
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_sqlite3.c
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_sqlite3.h
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_sqlite3.o
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_sqlite3_extension.c
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_sqlite3_extension.o
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/error.h
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/lib/do_sqlite3.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/lib/do_sqlite3/transaction.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/lib/do_sqlite3/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/command_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/connection_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/encoding_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/error/sql_error_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/reader_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/result_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/array_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/bigdecimal_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/boolean_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/byte_array_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/class_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/date_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/datetime_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/float_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/integer_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/nil_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/other_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/range_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/string_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/spec/typecast/time_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/tasks/compile.rake
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/tasks/release.rake
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/tasks/retrieve.rake
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/tasks/spec.rake
/usr/lib64/ruby/gems/2.3.0/specifications/do_sqlite3-0.10.17.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/do_sqlite3-0.10.17/do_sqlite3/do_sqlite3.so
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/ext/do_sqlite3/do_sqlite3.so
/usr/lib64/ruby/gems/2.3.0/gems/do_sqlite3-0.10.17/lib/do_sqlite3/do_sqlite3.so
