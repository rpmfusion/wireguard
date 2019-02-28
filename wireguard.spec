Name:           wireguard
Summary:        Fast, modern, secure VPN tunnel
Version:        0.0.20190227
Release:        1%{?dist}
License:        GPLv2

URL:            https://www.wireguard.com/
Source0:        https://git.zx2c4.com/WireGuard/snapshot/WireGuard-%{version}.tar.xz

%{?systemd_requires}
BuildRequires:  systemd
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libmnl)

Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and utilizes 
state-of-the-art cryptography. It aims to be faster, simpler, leaner, 
and more useful than IPSec, while avoiding the massive headache. It intends 
to be considerably more performant than OpenVPN. WireGuard is designed as a 
general purpose VPN for running on embedded interfaces and super computers 
alike, fit for many different circumstances. It runs over UDP.


%prep
%autosetup -n WireGuard-%{version} different circumstances. It runs over UDP.

# Remove .gitignore files in examples
find contrib/ -type f -name ".gitignore" -exec rm "{}" \;
# Do not use /usr/bin/env
sed -i '1s@/usr/bin/env bash@/bin/bash@' contrib/examples/ncat-client-server/client-quick.sh
# Use standard perms for /etc/wireguard
sed -i 's|install -v -m 0700|install -v -m 0755|' src/tools/Makefile


%build
%set_build_flags

pushd contrib/examples/dns-hatchet
sh apply.sh
popd

pushd src/tools
%make_build V=1
popd


%install
pushd src/tools
%make_install
popd


%post
%systemd_post wg-quick@.service


%preun
%systemd_preun wg-quick@.service


%postun
%systemd_postun_with_restart wg-quick@.service


%files
%doc contrib/examples README.md
%license COPYING
%{_bindir}/wg
%{_bindir}/wg-quick
%{_sysconfdir}/wireguard
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick
%{_unitdir}/wg-quick@.service
%{_mandir}/man8/wg.8*
%{_mandir}/man8/wg-quick.8*


%changelog
* Thu Feb 28 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190227-1
- Release 0.0.20190227

* Tue Feb 19 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190123-1
- Release 0.0.20190123

* Tue Dec 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181218-1
- Release 0.0.20181218

* Mon Nov 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181119-1
- Release 0.0.20181119

* Fri Nov 16 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181115-1
- Release 0.0.20181115

* Thu Oct 18 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181018-1
- Release 0.0.20181018

* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181007-1
- Release 0.0.20181007

* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20181006-1
- Release 0.0.20181006

* Tue Sep 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20180925-1
- Release 0.0.20180925

* Sun Sep 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20180918-1
- Initial package
