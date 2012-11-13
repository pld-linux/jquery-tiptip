%define		plugin	tiptip
Summary:	TipTip jQuery Plugin
Name:		jquery-%{plugin}
Version:	1.3
Release:	1
License:	MIT and GPL
Group:		Applications/WWW
Source0:	http://www.drewwilson.com/upload/data/4/tipTipv13.zip
# Source0-md5:	1ba6077aaac73d98a3ade81aefdb5e69
URL:		http://code.drewwilson.com/entry/tiptip-jquery-plugin
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	jquery >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
TipTip is a better way to make custom tooltips. It's very lightweight
(3.5KiB), uses zero images, and is fully customizable via CSS

%prep
%setup -qc

%build
install -d build

# pack .css
for css in *.css; do
	out=build/${css#*/jquery.}
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $css -o $out
%else
	cp -p $css $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.tipTip.minified.js  $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.tipTip.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

cp -p build/tipTip.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
cp -p tipTip.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
