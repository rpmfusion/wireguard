Name:           wireguard
Summary:        Fast, modern, secure VPN tunnel
Version:        0.0.20190227
Release:        3%{?dist}
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
%autosetup -n WireGuard-%{version}

# Remove .gitignore files in examples
find contrib/ -type f -name ".gitignore" -exec rm "{}" \;
# Do not use /usr/bin/env
sed -i '1s@/usr/bin/env bash@/bin/bash@' contrib/examples/ncat-client-server/client-quick.sh


%build
%set_build_flags
%make_build V=1 -C src/tools


%install
%make_install -C src/tools \
        WITH_BASHCOMPLETION=yes \
        WITH_WGQUICK=yes \
        WITH_SYSTEMDUNITS=yes


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
%{_unitdir}/wg-quick@.service
%{_sysconfdir}/wireguard
%{_mandir}/man8/wg.8*
%{_mandir}/man8/wg-quick.8*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick


%changelog
* Thu Mar 07 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.20190227-3
- Unifying spec with Lubomir Rintel's one
- Rebuilt for akmods-ostree-post scriptlet

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.20190227-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

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
