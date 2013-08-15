# Generated from httparty-0.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname httparty

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Makes http fun! Also, makes consuming restful web services dead easy
Name: rubygem-%{gemname}
Version: 0.11.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://jnunemaker.github.com/httparty
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: rubygem(multi_json) => 1.0
Requires: rubygem(multi_json) < 2
Requires: rubygem(multi_xml) >= 0.5.2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Makes http fun! Also, makes consuming restful web services dead easy.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%files
%defattr(-, root, root, -)
%{geminstdir}
%{_bindir}/httparty
%{geminstdir}/bin
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%doc %{gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Aug 14 2013  <bradejr@puppetlabs.com> - 0.11.0-1
- Initial package
